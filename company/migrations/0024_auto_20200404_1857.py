# Generated by Django 3.0.2 on 2020-04-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0023_auto_20200404_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='next',
            field=models.CharField(blank=True, choices=[('説明会', '説明会'), ('エントリー', 'エントリー'), ('レポート', 'レポート'), ('スライド', 'スライド'), ('エントリーシート', 'エントリーシート'), ('Webテスト', 'Webテスト'), ('コーディングテスト', 'コーディングテスト'), ('面談', '面談'), ('一次面接', '一次面接'), ('二次面接', '二次面接'), ('三次面接', '三次面接'), ('最終面接', '最終面接'), ('日程調整', '日程調整'), ('辞退', '辞退'), ('内定承諾', '内定承諾'), ('完了', '完了')], max_length=32, null=True, verbose_name='次のステップ'),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(blank=True, choices=[('説明会前', '説明会前'), ('面談前', '面談前'), ('テスト前', 'テスト前'), ('エントリー前', 'エントリー前'), ('一次面接前', '一次面接前'), ('二次面接前', '二次面接前'), ('三次面接前', '三次面接前'), ('最終面接前', '最終面接前'), ('結果待ち', '結果待ち'), ('内々定', '内々定'), ('内定', '内定'), ('お祈り', 'お祈り'), ('辞退', '辞退')], max_length=32, null=True, verbose_name='ステータス'),
        ),
    ]
