# Generated by Django 3.0.5 on 2022-02-18 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20220218_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbook',
            old_name='isbn',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='issuedbook',
            old_name='idClient',
            new_name='Client',
        ),
    ]
