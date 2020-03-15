from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Company(models.Model):
    posi_lis = ["Webエンジニア","データサイエンティスト","研究開発","ITコンサルタント","営業","企画","マーケティング"]
    positions = [(i,i) for i in posi_lis]

    status_lis = ["オンライン面談前","エントリー前","一次面接前","二次面接前","三次面接前","最終面接前","内定","お祈り"]
    statuses=[(i,i) for i in status_lis]

    next_lis = ['エントリー','エントリーシート','Webテスト','コーディングテスト','面接日程調整','内定承諾']
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
    total = models.IntegerField('従業員数', blank=True, null=True)
    memo = models.TextField('メモ', default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

    def get_list(self):
        return {'企業名':self.company, '従業員数': self.total, 'メモ': self.memo}


# Create your models here.
