from django.db import models

# Create your models here.


class Demo1(models.Model):
    name = models.CharField('姓名',max_length=200,)
    date = models.DateField('日期', blank=False)
    temperture = models.CharField('温度',default='正常',max_length=20)

