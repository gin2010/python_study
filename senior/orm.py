# -*- coding: utf-8 -*-
# File  : orm.py.py
# Author: water
# Date  : 2020/1/5
# Desc  : orm思想：对象-关系映射，用于操作mysql数据库
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        print("name--->",name)
        print("bases--->",bases)
        print("attrs--->",attrs)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,tuple):
                print("found mapping:{}==>{}".format(k,v))
                mappings[k] = v
        # 从字典中删除已经存储的属性
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls,name,bases,attrs)


class Model(metaclass=ModelMetaclass):

    def __init__(self,**kwargs):
        for name,value in kwargs.items():
            setattr(self,name,value)

    def save(self):
        fields = list()
        args = list()
        for k,v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self,k,None))

        # sql = 'insert into %s (%s) values (%s) ' %(self.__table__,','.join(fields),','.join([str(i) for i in args]))
        args_temp = list()
        for temp in args:
            if isinstance(temp,int):
                args_temp.append(str(temp))
            elif isinstance(temp,str):
                args_temp.append("""'%s'"""%temp)
        sql = 'insert into %s (%s) values (%s) ' %(self.__table__,','.join(fields),','.join(args_temp))
        print("sql:",sql)


class User(Model):
    # djange里面用的类来实现下面数据库表的列
    uid = ('uid','int unsigned')
    name = ("username","varchar(30)")
    email = ("email","varchar(30)")
    password = ("password","varchar(30)")
    # 当指定元素之后，以上的类属性就不在类中，而是在__mappings__中以字典存储
    # 因此此类中有
    # __mappings__ = {
    #     'uid':('uid','int unsigned'),
    #     'name':("username","varchar(30)"),
    #     'email':("email","varchar(30)"),
    #     'password':("password","varchar(30)")
    # }

def main():
    u = User(uid=12345,name="micheal",email="test@126.com",password="1234")
    u.save()

class Person(object):
    # 使用字典传参数直接初始化
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

    def eat(self):
        print('eat')

def setattr_main():
    p1 = Person(name='xiaoming',age=20,city="bj",gender="man")
    # print(p1.__dict__)
    print(p1.name)
    print(p1.city)


if __name__ == "__main__":
    # main()
    setattr_main()
