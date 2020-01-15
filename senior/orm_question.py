# -*- coding: utf-8 -*-
# File  : orm.py.py
# Author: water
# Date  : 2020/1/5
# Desc  : orm思想：对象-关系映射，用于操作mysql数据库

class ModelMetaclass(type):

    def __new__(cls,name,bases,attrs):
        mappings = dict() # 用于存放User中定义的变量
        print("--attrs--",attrs)
        for k,v in attrs.items():
            if isinstance(v,tuple): 
                # 如果改成if not k.startswith("__"):
                # 则会将Model类里的insert函数删除掉，导致 'User' has no attribute 'insert'
                print("found mapping:{}==>{}".format(k,v))
                mappings[k] = v
        print("--mappings11--->",mappings)
        # 从字典中删除已经存储的属性
        for k in mappings.keys():
            attrs.pop(k)
        print("-------mappings",mappings)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        print("attrs---->",attrs)
        return super().__new__(cls,name,bases,attrs)


class Model(metaclass=ModelMetaclass):
    '''
    将User实例对象的值u的值组成args_temp，传入到sql语句
    '''
    def __init__(self,**kwargs):
        # print("kwargs---> ",kwargs)
        for name,value in kwargs.items():
            setattr(self,name,value)

    def insert(self):
        fields = list()
        args = list()
        for k,v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self,k,None))

        args_temp = list()
        for temp in args:
            if isinstance(temp,int):
                args_temp.append(str(temp))
            elif isinstance(temp,str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s) ' %(self.__table__,','.join(fields),','.join(args_temp))
        print("sql:",sql)


# 应用Model来操作数据库
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
    u.insert()
    # print(u.__class__)
    # print(User.__class__)

if __name__ == "__main__":
    main()

