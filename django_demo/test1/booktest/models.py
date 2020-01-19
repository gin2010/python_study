from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """图书馆模型类orm"""
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        # 正常返回bookinfo object，修改此方法显示为其他内容
        return self.btitle

class HeroInfo(models.Model):
    '''英雄人物类书
        英雄名：hname
        性别：hgender
        年龄：hage
        备注：hcomment
    '''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    # hage = models.IntegerField()
    hcomment = models.CharField(max_length=128)
    # 增加外键
    hbook = models.ForeignKey("BookInfo")

    def __str__(self):
        return self.hname


