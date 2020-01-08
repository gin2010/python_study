from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """图书馆模型类orm"""
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

