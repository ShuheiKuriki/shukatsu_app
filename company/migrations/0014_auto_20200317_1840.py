# Generated by Django 3.0.2 on 2020-03-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20200316_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='total',
            new_name='salary',
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='member',
            field=models.IntegerField(blank=True, null=True, verbose_name='従業員数'),
        ),
    ]