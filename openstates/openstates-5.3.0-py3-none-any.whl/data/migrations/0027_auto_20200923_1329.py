# Generated by Django 3.0.5 on 2020-09-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0026_auto_20200923_1312"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventagendamedia",
            name="classification",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]
