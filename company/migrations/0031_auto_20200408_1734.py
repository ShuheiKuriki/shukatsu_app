# Generated by Django 3.0.2 on 2020-04-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0030_auto_20200408_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='next',
            field=models.CharField(blank=True, choices=[(0, '0.日程調整'), (1, '1.説明会'), (2, '2.エントリー'), (3, '3.レポート'), (4, '4.エントリーシート'), (5, '5.Webテスト'), (6, '6.コーディングテスト'), (7, '7.面談準備'), (8, '8.面接準備'), (9, '9.オファー面談前'), (10, '10.辞退'), (11, '11.内定承諾'), (12, '12.完了')], max_length=32, null=True, verbose_name='次のステップ'),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(blank=True, choices=[(0, '0.結果待ち'), (1, '1.説明会前'), (2, '2.カジュアル面談前'), (3, '3.エントリー前'), (4, '4.テスト前'), (5, '5.一次面接前'), (6, '6.二次面接前'), (7, '7.三次面接前'), (8, '8.最終面接前'), (9, '9.内々定'), (10, '10.オファー面談前'), (11, '11.内定'), (12, '12.お祈り'), (13, '13.辞退')], max_length=32, null=True, verbose_name='ステータス'),
        ),
    ]
