from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Company(models.Model):
    posi_lis = ["Webエンジニア","データサイエンティスト","研究開発","ITコンサルタント",
                    "システムエンジニア","営業","企画","マーケティング"]
    positions = [(i,i) for i in posi_lis]

    status_lis = ['結果待ち',"説明会後","カジュアル面談後","エントリー前","エントリー後","テスト通過",
                    "一次面接通過","二次面接通過","三次面接通過","内々定","内定","お祈り",'辞退済']
    statuses=[('0'+str(i)+'. '+s,s) if i<10 else (str(i)+'. '+s,s) for i,s in enumerate(status_lis)]

    next_lis = ['日程調整','説明会','エントリー','レポート','エントリーシート','Webテスト','コーディングテスト',
                '面談準備','面接準備','内定承諾','辞退','完了']
    nexts = [('0'+str(i)+'. '+s,s) if i<10 else (str(i)+'. '+s,s) for i,s in enumerate(next_lis)]

    # statuses=[(i,i) for i in status_lis]
    #
    # nexts = [(i,i) for i in next_lis]

    # next = models.CharField('次のステップ',choices=nexts,max_length=32, blank=True, null=True)
    # status = models.CharField('ステータス',choices=statuses,max_length=32, blank=True, null=True)

    desire_lis = ['A','B','C','D','E']
    desires = [(i,i) for i in desire_lis]

    name = models.CharField('企業名', max_length=256, blank=True)
    position = models.CharField('ポジション', choices=positions, max_length=32, blank=True, null=True)
    status = models.CharField('ステータス',choices=statuses, max_length=32, blank=True, null=True)
    next = models.CharField('次のステップ',choices=nexts, max_length=32, blank=True, null=True)
    deadline = models.DateField('期限', default=now, blank=True, null=True)
    desire = models.CharField('志望度', choices=desires,max_length=32, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CompanyInfo(models.Model):
    company = models.OneToOneField(Company, verbose_name='企業名', null=True, on_delete=models.CASCADE)
    official = models.CharField('正式名称',max_length=128, blank=True, null=True)
    member = models.IntegerField('従業員数', blank=True, null=True)
    industry = models.CharField('業界', max_length=128, blank=True, null=True)
    area = models.TextField('事業領域', blank=True, null=True)
    salary = models.TextField('給与', blank=True, null=True)
    mission = models.TextField('企業理念', blank=True, null=True)
    vision = models.TextField('ビジョン', blank=True, null=True)
    benefit = models.TextField('福利厚生', blank=True, null=True)
    place = models.TextField('勤務地', blank=True, null=True)
    working_time = models.TextField('勤務時間', blank=True, null=True)
    reason = models.TextField('志望理由', blank=True, null=True)
    specification = models.TextField('特徴', blank=True, null=True)
    questions = models.TextField('疑問点', blank=True, null=True)
    memo = models.TextField('メモ', default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

# Create your models here.
