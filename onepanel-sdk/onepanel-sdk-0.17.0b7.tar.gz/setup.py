# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Generated by: https://openapi-generator.tech
"""


import sys
import subprocess
from setuptools import setup, find_packages  # noqa: H301
from setuptools.command.install import install as InstallCommand

NAME = "onepanel-sdk"
VERSION = "0.17.0b7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

class Install(InstallCommand):
    """ Customized setuptools install command which uses pip. """

    def run(self, *args, **kwargs):
        subprocess.call([sys.executable, '-m', 'pip', 'install','git+https://github.com/couler-proj/couler'])
        InstallCommand.run(self, *args, **kwargs)

setup(
    name=NAME,
    version=VERSION,
    description="Python SDK for Onepanel",
    author="Onepanel, Inc.",
    author_email="support@onepanel.io",
    url="https://github.com/onepanelio/core",
    keywords=["onepanel", "computer-vision", "deep-learning", "ai", "mlops"],
    install_requires=REQUIRES,
    cmdclass={
        'install': Install,
    },
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    long_description="""\
    Python SDK for Onepanel - Production scale vision AI platform with fully integrated components for model building, automated labeling, data processing and model training pipelines.
    """
)
