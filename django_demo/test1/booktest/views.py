from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from booktest.models import BookInfo,HeroInfo
# Create your views here.


def index(request):
    # 进行url的处理，并返回内容
    temp_url = "booktest/index.html"
    context_dict = {'context':'测试参数',
                    "list":list(range(1,10)),
                    }
    return render(request,temp_url,context=context_dict)

# render函数就是实现下面功能的
# def index(request):
#     # 进行url的处理，并返回内容
#     # 1.加载模板文件
#     index_temp = loader.get_template("booktest/index.html")
#     # 2.定义模板上下文，给模板文件传递数据
#     context = RequestContext(request,{})
#     # 3.模板渲染，产生标准的html内容
#     res = index_temp.render(context)
#     # 4.res返回给浏览器
#     return HttpResponse(res)

def show_books(request):
    # 显示图书信息
    books = BookInfo.objects.all()
    temp_url = "booktest/show_books.html"
    context_dict = {'books':books}
    return render(request,template_name=temp_url,context=context_dict)

def details(request,bid):
    # 显示图书里面的英雄
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    temp_url = "booktest/details.html"
    context_dict = {'heros':heros,"book":book}
    return render(request, template_name=temp_url, context=context_dict)

def create(request):
    # 新增一本书
    pass
