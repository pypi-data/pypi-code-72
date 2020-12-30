# -*- coding: utf-8 -*-

"""Utilities and implementation for bioversions."""

import datetime
import ftplib
from dataclasses import dataclass
from typing import Any, ClassVar, Mapping, Optional, Union

import pystow
import requests
from bs4 import BeautifulSoup
from cachier import cachier
from dataclasses_json import dataclass_json

BIOVERSIONS_HOME = pystow.get('bioversions')


def norm(s: str) -> str:
    """Normalize a string for dictionary lookup."""
    return s.lower().replace(' ', '').replace('-', '').replace('.', '')


def get_soup(url: str) -> BeautifulSoup:
    """Get a beautiful soup parsed version of the given web page."""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    return soup


#: A decorator for functions whose return values
#: should be cached and refreshed once per day
refresh_daily = cachier(
    stale_after=datetime.timedelta(days=1),
    backend='memory',
    cache_dir=BIOVERSIONS_HOME,
)


class MetaGetter(type):
    """A metatype to expose two class properties."""

    _cache = None

    @property
    def _cache_prop(cls):
        if cls._cache is None:
            cls._cache = cls().get()
        return cls._cache

    @property
    def version(cls) -> str:
        """Get the version of the getter based on the inheriting class's implementation."""
        if isinstance(cls._cache_prop, str):
            return cls._cache_prop
        elif isinstance(cls._cache_prop, dict):
            return cls._cache_prop['version']
        else:
            raise TypeError

    @property
    def date(cls) -> Optional[str]:
        """Get the date if it's set."""
        if isinstance(cls._cache_prop, dict):
            return cls._cache_prop['date']

    @property
    def version_date_parsed(cls) -> Optional[datetime.date]:
        """Get the date as a parsed class there's a format string."""
        if cls.date_version_fmt:
            return datetime.datetime.strptime(cls.version, cls.date_version_fmt).date()

    @property
    def homepage(cls) -> Optional[str]:
        """Get the homepage's URL if a format string was specified."""
        if cls.homepage_fmt:
            version = cls.homepage_version_transform(cls.version)
            return cls.homepage_fmt.format(version=version)

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Transform the version for formatting into the homepage."""
        return version


@dataclass_json
@dataclass
class Bioversion:
    """A dataclass for information about a database and version."""

    #: The database name
    name: str
    #: The database current version
    version: str
    #: The date of the current release
    date: Optional[str]
    #: The URL for the homepage of the specific version of the database
    homepage: Optional[str]


class Getter(metaclass=MetaGetter):
    """A class for holding the name of a database and implementation of the version getter."""

    #: The name of the database. Specify this in the inheriting class!.
    name: ClassVar[str]
    #: The URL with `{version}` to format in the version. Specify this in the inheriting class.
    homepage_fmt: ClassVar[Optional[str]] = None
    date_version_fmt: ClassVar[Optional[str]] = None

    # The following two are automatically calculated based on the metaclass
    version: ClassVar[str]
    date: ClassVar[str]
    homepage: ClassVar[str]

    def get(self) -> Union[str, Mapping[str, str]]:
        """Get the latest of this database."""
        raise NotImplementedError

    @classmethod
    def print(cls, sep: str = '\t', file=None):
        """Print the latest version of this database."""
        x = [cls.name, cls.version]
        if cls.date:
            x.append(f'({cls.date})')
        if cls.homepage:
            x.append(cls.homepage)
        print(*x, sep=sep, file=file)

    @classmethod
    def resolve(cls) -> Bioversion:
        """Get a Bioversion data container with the data for this database."""
        return Bioversion(
            name=cls.name,
            version=cls.version,
            homepage=cls.homepage,
            date=cls.date,
        )

    @classmethod
    def to_dict(cls) -> Mapping[str, Any]:
        """Get a dict with the data for this database."""
        return cls.resolve().to_dict()


def get_obo_version(url: str) -> str:
    """Get the data version from an OBO file."""
    with requests.get(url, stream=True) as res:
        for line in res.iter_lines():
            line = line.decode('utf-8')
            if line.startswith('data-version:'):
                version = line[len('data-version:'):].strip()
                return version
    raise ValueError(f'No data-version line contained in {url}')


class OboGetter(Getter):
    """An implementation for getting OBO versions."""

    key: ClassVar[str]
    strip_key_prefix: ClassVar[bool] = False
    strip_version_prefix: ClassVar[bool] = False
    strip_file_suffix: ClassVar[bool] = False

    def get(self) -> str:
        """Get the OBO version."""
        url = f'http://purl.obolibrary.org/obo/{self.key}.obo'
        return self.process(get_obo_version(url))

    def process(self, version: str) -> str:
        """Post-process the version string."""
        if self.strip_key_prefix:
            version = version[len(f'{self.key}/'):]
        if self.strip_version_prefix:
            version = version[len('releases/'):]
        if self.strip_file_suffix:
            version = version[:-(len(self.key) + 5)]
        return version


def _get_ftp_version(host: str, directory: str) -> str:
    with ftplib.FTP(host) as ftp:
        ftp.login()
        ftp.cwd(directory)
        names = sorted([
            tuple(int(part) for part in name.split('.'))
            for name in ftp.nlst()
            if _is_version(name)
        ])
    return '.'.join(map(str, names[-1]))


def _get_ftp_date_version(host: str, directory: str) -> str:
    with ftplib.FTP(host) as ftp:
        ftp.login()
        ftp.cwd(directory)
        names = sorted([
            name
            for name in ftp.nlst()
            if _is_iso_8601(name)
        ])
    return names[-1]


def _is_iso_8601(s: str) -> bool:
    s = s.split('-')
    return len(s) == 3 and s[0].isnumeric() and s[1].isnumeric() and s[2].isnumeric()


def _is_version(s: str) -> bool:
    s = s.split('.')
    return len(s) == 2 and s[0].isnumeric() and s[1].isnumeric()


def _is_semantic_version(s: str) -> bool:
    s = s.split('.')
    return len(s) == 3 and s[0].isnumeric() and s[1].isnumeric() and s[2].isnumeric()
