# Generated by Django 3.0.2 on 2020-03-15 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20200316_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='my_status',
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='企業名'),
        ),
    ]