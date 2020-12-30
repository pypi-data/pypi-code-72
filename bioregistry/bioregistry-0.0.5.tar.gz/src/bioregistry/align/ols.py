# -*- coding: utf-8 -*-

"""Align the OLS with the Bioregistry."""

from ..external import get_ols
from ..utils import norm, updater


def _prepare_ols(ols_entry):
    ols_id = ols_entry['ontologyId']
    config = ols_entry['config']

    license_value = config['annotations'].get('license', [None])[0]
    if license_value in {'Unspecified', 'Unspecified'}:
        license_value = None

    rv = {
        'prefix': ols_id,
        'name': config['title'],
        'download': config['fileLocation'],
        'version': config['version'],
        'version.iri': config['versionIri'],
        'description': config['description'],
        'license': license_value,
    }

    rv = {k: v for k, v in rv.items() if v}
    return rv


@updater
def align_ols(registry):
    """Update OLS references."""
    ols_id_to_bioregistry_id = {
        entry['ols']['prefix']: key
        for key, entry in registry.items()
        if 'ols' in entry
    }

    ols_registry = get_ols(mappify=True)

    ols_norm_prefix_to_prefix = {
        norm(obo_key): obo_key
        for obo_key in ols_registry
    }
    for bioregistry_id, entry in registry.items():
        if 'ols' in entry:
            continue
        ols_id = ols_norm_prefix_to_prefix.get(norm(bioregistry_id))
        if ols_id is not None:
            entry['ols'] = {'prefix': ols_id}
            ols_id_to_bioregistry_id[ols_id] = bioregistry_id

    for ols_prefix, ols_entry in ols_registry.items():
        bioregistry_id = ols_id_to_bioregistry_id.get(ols_prefix)
        if bioregistry_id is None:
            continue
        registry[bioregistry_id]['ols'] = _prepare_ols(ols_entry)


if __name__ == '__main__':
    align_ols()
