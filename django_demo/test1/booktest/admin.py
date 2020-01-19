from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# Register your models here.

# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书管理类'''

    list_display = ['id','btitle','bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    '''英雄管理类'''

    list_display = ['id','hname','hcomment']


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
# admin.site.register(HeroInfo)