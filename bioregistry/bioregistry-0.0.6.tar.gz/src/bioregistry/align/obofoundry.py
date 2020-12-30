# -*- coding: utf-8 -*-

"""Align the OBO Foundry with the Bioregistry."""

import click
import requests
import requests_ftp

from ..external import get_obofoundry
from ..utils import norm, updater

requests_ftp.monkeypatch_session()
session = requests.Session()

OBO_KEYS = {
    'id',
    'prefix',
    'pattern',
    'namespaceEmbeddedInLui',
    'name',
    'deprecated',
    'description',
}


def _prepare_obo(obofoundry_entry):
    prefix = obofoundry_entry['id']
    rv = {
        'prefix': prefix,
        'name': obofoundry_entry['title'],
        'deprecated': obofoundry_entry.get('is_obsolete', False),
    }

    license_dict = obofoundry_entry.get('license')
    if license_dict is not None:
        rv['license'] = license_dict['label']

    contact_dict = obofoundry_entry.get('contact')
    if contact_dict is not None and contact_dict.get('email'):
        rv.update({
            'contact': contact_dict['email'],
            'contact.label': contact_dict['label'],
        })

    build = obofoundry_entry.get('build')
    if build is not None:
        method = build.get('method')
        if method is None and 'checkout in build':
            method = 'vcs'
        if method is None:
            click.echo(f'[{prefix}] missing method: {build}')
            return rv

        if method == 'vcs':
            if build['system'] != 'git':
                click.echo(f'[{prefix}] Unrecognized build system: {build["system"]}')
                return rv
            checkout = build['checkout'].replace('  ', ' ')
            if not checkout.startswith('git clone https://github.com/'):
                click.echo(f'[{prefix}] unhandled build checkout: {checkout}')
                return rv

            owner, repo = checkout.removeprefix('git clone https://github.com/').removesuffix('.git').split('/')
            rv['repo'] = f'https://github.com/{owner}/{repo}.git'

            path = build.get('path', '.')
            if path == '.':
                obo_url = f'https://raw.githubusercontent.com/{owner}/{repo}/master/{prefix}.obo'
            else:  # disregard the path since most repos don't actually use it anyway
                # TODO maybe try recovering if this doesn't work
                obo_url = f'https://raw.githubusercontent.com/{owner}/{repo}/master/{prefix}.obo'

            res = session.get(obo_url)
            if res.status_code == 200:
                rv['download.obo'] = obo_url
            else:
                click.secho(f"[{prefix}] [http {res.status_code}] see {rv['repo']} [{path}]", bold=True, fg='red')

        elif method == 'owl2obo':
            source_url = build['source_url']

            # parse repo if possible
            for url_prefix in ('https://github.com/', 'http://github.com/', 'https://raw.githubusercontent.com/'):
                if source_url.startswith(url_prefix):
                    owner, repo, *_ = source_url.removeprefix(url_prefix).split('/')
                    rv['repo'] = f'https://github.com/{owner}/{repo}.git'
                    break

            if source_url.endswith('.obo'):
                rv['download.obo'] = source_url
            elif source_url.endswith('.owl'):
                obo_url = source_url.removesuffix('.owl') + '.obo'
                res = session.get(obo_url)
                if res.status_code == 200:
                    rv['download.obo'] = source_url
                else:
                    click.secho(f'[{prefix}] [http {res.status_code}] problem with {obo_url}', bold=True, fg='red')
            else:
                click.echo(f'[{prefix}] unhandled build.source_url: {source_url}')

        elif method == 'obo2owl':
            source_url = build['source_url']
            if source_url.endswith('.obo'):
                res = session.get(source_url)
                if res.status_code == 200:
                    rv['download.obo'] = source_url
                else:
                    click.secho(f'[{prefix}] [http {res.status_code}] problem with {source_url}', bold=True, fg='red')
            else:
                click.secho(f'[{prefix}] unhandled extension {source_url}', bold=True, fg='red')
        else:
            click.echo(f'[{prefix}] unhandled build method: {method}')

    return rv


@updater
def align_obofoundry(registry):
    """Update OBOFoundry references."""
    obofoundry_id_to_bioregistry_id = {
        entry['obofoundry']['prefix']: key
        for key, entry in registry.items()
        if 'obofoundry' in entry
    }
    obofoundry_registry = get_obofoundry(mappify=True)

    obofoundry_norm_prefix_to_prefix = {
        norm(obo_key): obo_key
        for obo_key in obofoundry_registry
    }
    for bioregistry_id, entry in registry.items():
        if 'obofoundry' in entry:
            continue
        obofoundry_id = obofoundry_norm_prefix_to_prefix.get(norm(bioregistry_id))
        if obofoundry_id is not None:
            entry['obofoundry'] = {'prefix': obofoundry_id}
            obofoundry_id_to_bioregistry_id[obofoundry_id] = bioregistry_id

    for obofoundry_prefix, obofoundry_entry in obofoundry_registry.items():
        # Get key by checking the miriam.id key
        bioregistry_id = obofoundry_id_to_bioregistry_id.get(obofoundry_prefix)
        if bioregistry_id is None:
            continue
        # click.echo(f'bioregistry={bioregistry_id}, obo={obofoundry_prefix}')
        registry[bioregistry_id]['obofoundry'] = _prepare_obo(obofoundry_entry)


if __name__ == '__main__':
    align_obofoundry()
