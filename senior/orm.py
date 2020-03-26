# -*- coding: utf-8 -*-
# File  : orm.py.py
# Author: water
# Date  : 2020/1/5
# Desc  : orm思想：对象-关系映射，用于操作mysql数据库
class ModelMetaclass(type):
    '''
    实现了一个功能：将User里的变量及值组成字典写入到__mappings__，将表名写到__table__里。
    只有通过元类，才能将User类中的所有变量及值取出来。
    attrs--->{'__mappings__': {
                'uid': ('uid', 'int unsigned'),
                'name': ('username', 'varchar(30)'),
                'email': ('email', 'varchar(30)'),
                'password': ('password', 'varchar(30)')
                },
            '__table__': 'User'}
    '''
    def __new__(cls,name,bases,attrs):
        print("name--->",name)
        print("bases--->",bases)
        print("attrs--->",attrs)
        mappings = dict() # 用于存放User中定义的变量
        for k,v in attrs.items():
            if isinstance(v,tuple):
                print("found mapping:{}==>{}".format(k,v))
                mappings[k] = v
        # 从字典中删除已经存储的属性
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        print("attrs---->",attrs)
        return type.__new__(cls,name,bases,attrs)


class Model(metaclass=ModelMetaclass):
    '''
    将User实例对象的值u的值组成args_temp，传入到sql语句
    '''
    def __init__(self,**kwargs):
        print("model kwargs---> ",kwargs)
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
    u.__dict__
    u.save()

# 下面只是尝试参数批量初始化--setattr使用
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


# 第三--自己再次深度orm实现20200301
# @Desc :orm实现思路
#       1.执行m = Man()时，分别对Person、Man进行创建对象(new对象)，因此都调PersonMetaClass中__new__，
#       2.只有Man对象调用__new__时，attrs字典里才有：{'name': 'man_name', 'age': 'man_age'}，
#       3.将上述值单独保存为了 __mysql__：{'name': 'man_name', 'age': 'man_age'}，必须用魔法方法__XXX__方式；
#       4.
import copy
class PersonMetaClass(type):
    def __new__(cls, name, base, attrs):
        # 1.分别对Person、Man进行创建对象
        d = dict()
        attrs_copy = copy.deepcopy(attrs)
        # print('name->',name)
        # print('attrs->',attrs)
        #-->{'__qualname__': 'Man', 'name': 'man_name', 'age': 'man_age'}
        for key in attrs_copy.keys():
            if not key.startswith("__") and isinstance(attrs[key],str):
                d[key] = attrs[key]
                attrs.pop(key)
        attrs['__mysql__'] = d # 必须用这种魔法方法的命名方式
        attrs["__table__"] = name
        # print("new---attrs:",attrs)
        return type.__new__(cls,name,base,attrs)


class Person(metaclass=PersonMetaClass):
    # 使用字典传参数直接初始化
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v) # 获取值时对应getattr

    def insert(self):

        # print(Man.__dict__) #这样可以取到
        print(self.__mysql__) # 否则只能用魔法方法的格式
        fields = list() #数据库字段
        values = list() #对应字段值
        for k in self.__mysql__.keys():
            fields.append(self.__mysql__[k])
            values.append(getattr(self,k))
        print('inset into {} {} values {}'.format(self.__table__,tuple(fields),tuple(values)))

class Man(Person):
    name = 'man_name'
    age = 'man_age'


def main_orm():
    m = Man(name='xiaoming',age=22)
    m.insert()


if __name__ == "__main__":
    # main()
    # setattr_main()
    main_magic()