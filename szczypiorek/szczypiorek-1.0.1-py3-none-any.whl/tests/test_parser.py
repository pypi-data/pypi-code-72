
from unittest.mock import call
import textwrap
import os

import pytest
import click

import szczypiorek as env
from szczypiorek.parser import Env
from szczypiorek.exceptions import ValidatorError
from szczypiorek.crypto import encrypt
from tests import BaseTestCase


class EnvTestCase(BaseTestCase):

    #
    # __INIT__
    #
    def test__init__(self):

        e = Env(is_prod=True, secret_key='hello')

        assert e.is_prod is True
        assert e.secret_key == 'hello'


class EnvParserTestCase(BaseTestCase):

    def setUp(self):
        super(EnvParserTestCase, self).setUp()
        env.EnvParser._envs_cache = {}
        try:
            del os.environ['SZCZYPIOREK_PATH']

        except KeyError:
            pass

    def test_parse(self):

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField()

            is_important = env.BooleanField()

            aws_url = env.URLField()

            number_of_workers = env.IntegerField()

        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: true
            aws:
              url: http://hello.word.org

            number:
              of:
                workers: '113'
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        e = MyEnvParser().parse()

        assert e.secret_key == 'secret.whatever'
        assert e.is_important is True
        assert e.aws_url == 'http://hello.word.org'
        assert e.number_of_workers == 113

    def test_parse__as_env(self):

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField(max_length=24, as_env=True)

            is_important = env.BooleanField()

            aws_url = env.URLField(as_env='AWS_URL_WHAT')

            number_of_workers = env.IntegerField()

        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: true
            aws:
              url: http://hello.word.org

            number:
              of:
                workers: '113'
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        e = MyEnvParser().parse()

        assert e.secret_key == 'secret.whatever'
        assert e.is_important is True
        assert e.aws_url == 'http://hello.word.org'
        assert e.number_of_workers == 113
        assert os.environ['SECRET_KEY'] == 'secret.whatever'
        assert os.environ['AWS_URL_WHAT'] == 'http://hello.word.org'
        del os.environ['SECRET_KEY']
        del os.environ['AWS_URL_WHAT']

    def test_parse__as_file(self):

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField(max_length=24, as_file='secret.yml')

            is_important = env.BooleanField()

            aws_url = env.URLField(as_file=True)

            number_of_workers = env.IntegerField()

        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: true
            aws:
              url: http://hello.word.org

            number:
              of:
                workers: '113'
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        e = MyEnvParser().parse()

        assert e.secret_key == 'secret.whatever'
        assert e.is_important is True
        assert e.aws_url == 'http://hello.word.org'
        assert e.number_of_workers == 113
        assert self.root_dir.join('secret.yml').read() == 'secret.whatever'
        assert self.root_dir.join('aws_url').read() == 'http://hello.word.org'

    def test_parse__singleton__same_gpg_file(self):

        secho = self.mocker.patch.object(click, 'secho')

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField()

            is_important = env.BooleanField()

        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: true
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        for i in range(3):
            e = MyEnvParser().parse()

            assert e.secret_key == 'secret.whatever'
            assert e.is_important is True

        assert secho.call_count == 1

    def test_parse__singleton__different_gpg_file(self):

        secho = self.mocker.patch.object(click, 'secho')

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField()

            is_important = env.BooleanField()

        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: true
        '''))
        self.root_dir.join('integration.gpg').write(content, mode='w')
        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: false
        '''))
        self.root_dir.join('production.gpg').write(content, mode='w')

        cases = [
            'integration.gpg',
            'production.gpg',
            'integration.gpg',
            'integration.gpg',
            'production.gpg',
            'production.gpg',
            'production.gpg',
        ]

        for gpg in cases:
            os.environ['SZCZYPIOREK_PATH'] = str(self.root_dir.join(gpg))
            MyEnvParser().parse()

        int_path = str(self.root_dir.join('integration.gpg'))
        prod_path = str(self.root_dir.join('production.gpg'))
        assert secho.call_args_list == [
            call(f'[LOADING] {int_path}', color='green'),
            call(f'[LOADING] {prod_path}', color='green'),
        ]

    def test_parse__complex_example(self):

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField()

            is_important = env.BooleanField()

            aws_url = env.URLField()

            number_of_workers = env.IntegerField()

        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: true
            aws:
              url: {{ a.b.c }}

            number:
              of:
                workers: '113'
            a:
              b:
                c: http://hello.word.org
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        e = MyEnvParser().parse()

        assert e.secret_key == 'secret.whatever'
        assert e.is_important is True
        assert e.aws_url == 'http://hello.word.org'
        assert e.number_of_workers == 113

    def test_parse__optional_with_defaults(self):

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField(required=False, default='hello')

            is_important = env.BooleanField(required=False, default=False)

            aws_url = env.URLField(required=False, default='http://hi.pl')

            number_of_workers = env.IntegerField(required=False, default=12)

        content = encrypt(textwrap.dedent('''
            what:
              event: yo
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        e = MyEnvParser().parse()

        assert e.secret_key == 'hello'
        assert e.is_important is False
        assert e.aws_url == 'http://hi.pl'
        assert e.number_of_workers == 12

    def test_parse__optional_without_defaults(self):

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField(required=False, allow_null=True)

            is_important = env.BooleanField(required=False, allow_null=True)

            aws_url = env.URLField(required=False, allow_null=True)

            number_of_workers = env.IntegerField(
                required=False, allow_null=True)

        content = encrypt(textwrap.dedent('''
            what:
              event: yo
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        e = MyEnvParser().parse()

        assert e.secret_key is None
        assert e.is_important is None
        assert e.aws_url is None
        assert e.number_of_workers is None

    def test_parse__validation_errors(self):

        class MyEnvParser(env.EnvParser):

            secret_key = env.CharField(max_length=12)

            is_important = env.BooleanField()

            aws_url = env.URLField()

            number_of_workers = env.IntegerField()

        content = encrypt(textwrap.dedent('''
            secret:
              key: secret.whatever
            is_important: whatever
            aws:
              url: not.url

            number:
              of:
                workers: not.number
        '''))
        self.root_dir.join('env.gpg').write(content, mode='w')

        with pytest.raises(ValidatorError) as e:
            MyEnvParser().parse()

        assert e.value.args[0] == (
            'env.aws_url: Text "not.url" is not valid URL')
