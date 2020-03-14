from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField('企業名', max_length=256, blank=True)
    lis = ["エントリー前","一次面接前","二次面接前","最終面接前","内定","落選"]
    statuses=[(i,i) for i in lis]
    status = models.CharField('ステータス',choices=statuses,max_length=128,blank=True, null=True)
    memo = models.TextField('メモ', default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
