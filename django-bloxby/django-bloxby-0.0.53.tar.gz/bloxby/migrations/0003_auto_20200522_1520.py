# Generated by Django 3.0.6 on 2020-05-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloxby', '0002_page_template_templateasset'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='remote_id',
            field=models.IntegerField(blank=True, help_text='ID of the template on the remote server.', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
