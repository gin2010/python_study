from django.contrib import admin
from .models import Demo1
# Register your models here.


class Demo1Admin(admin.ModelAdmin):

    list_display = ('name','date','temperture')
    # list_filter = ['date',]  # 界面右侧加过滤器
    search_fields = ['name']  # 界面上面加搜索框

admin.site.register(Demo1,Demo1Admin)