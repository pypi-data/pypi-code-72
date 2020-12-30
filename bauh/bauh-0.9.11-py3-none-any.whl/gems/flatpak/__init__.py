import os
from pathlib import Path

from bauh.api.constants import CONFIG_PATH
from bauh.commons import resource

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SUGGESTIONS_FILE = 'https://raw.githubusercontent.com/vinifmor/bauh-files/master/flatpak/suggestions.txt'
CONFIG_FILE = '{}/flatpak.yml'.format(CONFIG_PATH)
CONFIG_DIR = '{}/flatpak'.format(CONFIG_PATH)
UPDATES_IGNORED_FILE = '{}/updates_ignored.txt'.format(CONFIG_DIR)
EXPORTS_PATH = '{}/.local/share/flatpak/exports/share'.format(str(Path.home()))


def get_icon_path() -> str:
    return resource.get_path('img/flatpak.svg', ROOT_DIR)
