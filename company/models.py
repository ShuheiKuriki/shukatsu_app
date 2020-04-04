from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Company(models.Model):
    posi_lis = ["Webエンジニア","データサイエンティスト","研究開発","ITコンサルタント",
        "システムエンジニア","営業","企画","マーケティング"]
    positions = [(i,i) for i in posi_lis]

    status_lis = ["説明会前","面談前","テスト前","エントリー前","一次面接前","二次面接前",
            "三次面接前","最終面接前",'結果待ち',"内々定","内定","お祈り"]
    statuses=[(i,i) for i in status_lis]

    next_lis = ['説明会','エントリー','レポート','スライド','エントリーシート','Webテスト','コーディングテスト','面談',
                '一次面接','二次面接','三次面接','最終面接','日程調整','内定辞退','内定承諾']
    nexts = [(i,i) for i in next_lis]

    desire_lis = ['A','B','C','D','E']
    desires = [(i,i) for i in desire_lis]

    name = models.CharField('企業名', max_length=256, blank=True)
    position = models.CharField('ポジション', choices=positions, max_length=32, blank=True, null=True)
    status = models.CharField('ステータス',choices=statuses,max_length=32, blank=True, null=True)
    next = models.CharField('次のステップ',choices=nexts,max_length=32, blank=True, null=True)
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
    salary = models.TextField('給与', blank=True, null=True)
    mission = models.TextField('企業理念', blank=True, null=True)
    vision = models.TextField('ビジョン', blank=True, null=True)
    reason = models.TextField('志望理由', blank=True, null=True)
    memo = models.TextField('メモ', default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

# Create your models here.
