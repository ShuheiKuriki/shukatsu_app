from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Company(models.Model):
    name = models.CharField('企業名', max_length=256, blank=True)
    status_lis = ["エントリー前","一次面接前","二次面接前","最終面接前","内定","落選"]
    statuses=[(i,i) for i in status_lis]
    status = models.CharField('ステータス',choices=statuses,max_length=128,blank=True, null=True)
    next_lis = ['エントリー','エントリーシート','Webテスト','コーディングテスト','面接日程調整']
    nexts = [(i,i) for i in next_lis]
    next = models.CharField('次のステップ',choices=nexts,max_length=128,blank=True, null=True)
    deadline = models.DateField('期限', default=now, blank=True, null=True)
    memo = models.TextField('メモ', default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
