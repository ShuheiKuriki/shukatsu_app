# Generated by Django 3.0.2 on 2020-04-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0031_auto_20200408_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='next',
            field=models.CharField(blank=True, choices=[('0.日程調整', '日程調整'), ('1.説明会', '説明会'), ('2.エントリー', 'エントリー'), ('3.レポート', 'レポート'), ('4.エントリーシート', 'エントリーシート'), ('5.Webテスト', 'Webテスト'), ('6.コーディングテスト', 'コーディングテスト'), ('7.面談準備', '面談準備'), ('8.面接準備', '面接準備'), ('9.オファー面談前', 'オファー面談前'), ('10.辞退', '辞退'), ('11.内定承諾', '内定承諾'), ('12.完了', '完了')], max_length=32, null=True, verbose_name='次のステップ'),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(blank=True, choices=[('0.結果待ち', '結果待ち'), ('1.説明会前', '説明会前'), ('2.カジュアル面談前', 'カジュアル面談前'), ('3.エントリー前', 'エントリー前'), ('4.テスト前', 'テスト前'), ('5.一次面接前', '一次面接前'), ('6.二次面接前', '二次面接前'), ('7.三次面接前', '三次面接前'), ('8.最終面接前', '最終面接前'), ('9.内々定', '内々定'), ('10.オファー面談前', 'オファー面談前'), ('11.内定', '内定'), ('12.お祈り', 'お祈り'), ('13.辞退', '辞退')], max_length=32, null=True, verbose_name='ステータス'),
        ),
    ]
