# -*- coding: utf-8 -*-
# @Date : 2020-01-07
# @Author : water
# @Version  : v1.0
# @Desc  : call功能应用及用类的实例对象来做装饰器
# call应用一
class Animal(object):

    def __call__(self, words):
        print("Hello: ", words)


def main1():
    cat = Animal()
    cat("I am cat!")

# call应用二
class WSGIapp(object):
    def __init__(self):
        self.routes = {}

    def route(self,path=None):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def __call__(self,environ,start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            status = '200 OK'
            response_headers = [('Content-Type','text/plain')]
            start_response(status,response_headers)
            return self.routes[path]()
        else:
            status = '404 Not Found'
            response_headers = [('Content-Type','text/plain')]
            start_response(status,response_headers)
            return '404 Not Found!'


app = WSGIapp()

@app.route('/')
def index():
    print('index')

@app.route('/hello')
def hello():
    print('hello world')


if __name__ == "__main__":
    # main1()
    main2()