# Generated by Django 3.0.2 on 2020-03-15 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0010_auto_20200316_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='memo',
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='企業名'),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
