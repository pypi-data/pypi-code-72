from __future__ import print_function

import shlex
import subprocess
import sys

from setuptools import find_packages


version = '0.1.5'


if sys.argv[-1] == 'release':
    # Release via github-actions.
    commands = [
        'git tag v{:s}'.format(version),
        'git push origin master --tag',
    ]
    for cmd in commands:
        print('+ {}'.format(cmd))
        subprocess.check_call(shlex.split(cmd))
    sys.exit(0)

setup_requires = [
]

install_requires = [
    'scikit-build',
    'trimesh>=3.5.20'
]

setup_params = dict(
    name="pysdfgen",
    version=version,
    description="SDFGen for Python",
    author='iory',
    author_email='ab.ioryz@gmail.com',
    url='https://github.com/iory/pySDFGen',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(),
    setup_requires=setup_requires,
    install_requires=install_requires,
)


# https://github.com/skvark/opencv-python/blob/master/setup.py
def install_packages(*requirements):
    # No more convenient way until PEP 518 is implemented;
    # setuptools only handles eggs
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install"] + list(requirements)
    )


# https://github.com/skvark/opencv-python/blob/master/setup.py
def get_or_install(name, version=None):
    """If a package is already installed, build against it. If not, install

    """
    # Do not import 3rd-party modules into the current process
    import json
    js_packages = json.loads(
        # valid names & versions are ASCII as per PEP 440
        subprocess.check_output(
            [sys.executable,
             "-m", "pip", "list", "--format", "json"]).decode('ascii'))
    try:
        [package] = (package for package in js_packages
                     if package['name'] == name)
    except ValueError:
        install_packages("%s==%s" % (name, version) if version else name)
        return version
    else:
        return package['version']


def main():
    get_or_install('scikit-build')
    import skbuild  # NOQA

    skbuild.setup(**setup_params)


if __name__ == '__main__':
    main()
