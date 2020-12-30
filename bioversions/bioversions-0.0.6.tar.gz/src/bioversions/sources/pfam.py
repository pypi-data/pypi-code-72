# -*- coding: utf-8 -*-

"""A getter for Rfam."""

import ftplib

from bioversions.utils import Getter, _is_version

__all__ = [
    'PfamGetter',
]


class PfamGetter(Getter):
    """A getter for Pfam."""

    name = 'Pfam'
    homepage_fmt = 'ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam{version}/'

    def get(self):
        """Get the latest Pfam version number."""
        with ftplib.FTP('ftp.ebi.ac.uk') as ftp:
            ftp.login()
            ftp.cwd('pub/databases/Pfam/releases/')
            names = [
                name.removeprefix('Pfam')
                for name in ftp.nlst()
                if name.startswith('Pfam')
            ]
            names = sorted([
                tuple(int(part) for part in name.split('.'))
                for name in names
                if _is_version(name)
            ])
        return '.'.join(map(str, names[-1]))


if __name__ == '__main__':
    PfamGetter.print()
