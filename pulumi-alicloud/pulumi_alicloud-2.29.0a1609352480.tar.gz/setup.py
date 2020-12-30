# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'alicloud', '2.29.0-alpha.1609352480+c6a41e7b'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print("""
                There was an error installing the alicloud resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource alicloud 2.29.0-alpha.1609352480+c6a41e7b`
                """)
            else:
                raise


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(name='pulumi_alicloud',
      version='2.29.0a1609352480',
      description="A Pulumi package for creating and managing AliCloud resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      keywords='pulumi alicloud',
      url='https://pulumi.io',
      project_urls={
          'Repository': 'https://github.com/pulumi/pulumi-alicloud'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'pulumi_alicloud': [
              'py.typed'
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=2.9.0,<3.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
