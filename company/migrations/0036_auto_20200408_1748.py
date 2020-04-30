# Generated by Django 3.0.2 on 2020-04-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0035_auto_20200408_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(blank=True, choices=[('0. 結果待ち', '結果待ち'), ('1. 説明会後', '説明会後'), ('2. カジュアル面談後', 'カジュアル面談後'), ('3. エントリー前', 'エントリー前'), ('4. エントリー後', 'エントリー後'), ('5. テスト通過', 'テスト通過'), ('6. 一次面接通過', '一次面接通過'), ('7. 二次面接通過', '二次面接通過'), ('8. 三次面接通過', '三次面接通過'), ('9. 内々定', '内々定'), ('10. 内定', '内定'), ('11. お祈り', 'お祈り'), ('12. 辞退済', '辞退済')], max_length=32, null=True, verbose_name='ステータス'),
        ),
    ]