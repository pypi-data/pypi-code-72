import sys

from django.core.management import call_command

from boot_django import boot_django

boot_django()
call_command("filemetadata_index", *sys.argv[1:])
