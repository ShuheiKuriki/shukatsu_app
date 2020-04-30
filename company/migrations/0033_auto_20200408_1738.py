# Generated by Django 3.0.2 on 2020-04-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0032_auto_20200408_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='next',
            field=models.CharField(blank=True, choices=[('0. 日程調整', '日程調整'), ('1. 説明会', '説明会'), ('2. エントリー', 'エントリー'), ('3. レポート', 'レポート'), ('4. エントリーシート', 'エントリーシート'), ('5. Webテスト', 'Webテスト'), ('6. コーディングテスト', 'コーディングテスト'), ('7. 面談準備', '面談準備'), ('8. 面接準備', '面接準備'), ('9. 辞退', '辞退'), ('10. 内定承諾', '内定承諾'), ('11. 完了', '完了')], max_length=32, null=True, verbose_name='次のステップ'),
        ),
    ]