# Generated by Django 3.0.2 on 2020-03-15 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20200315_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='positions',
            new_name='position',
        ),
    ]