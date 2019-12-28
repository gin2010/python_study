# 创建jd数据库
create database jd1 charset=utf8;
# 查看全部的数据库
# show databases;
# 删除jd1的数据库
# drop database jd1; 
# 创建表goods
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
);
# 创建表时直接增加外键
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_id int not signed not null,
    brand_id int not signed not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0，
    FOREIGN KEY (case_id) REFERENCES goods_cates(id),
    FOREIGN KEY (brand_id) REFERENCES goods_brands(id)
);

# 插入商品数据
insert into goods values(0,'r510vn 15.6寸笔记本','笔记本','华硕','3399',default,default);
insert into goods values(0,'y400n 14.0寸笔记本','笔记本','联想','4999',default,default);
insert into goods values(0,'g150th 15.6寸笔记本','游戏本','雷神','8499',default,default);
insert into goods values(0,'x550cc 15.6寸笔记本','笔记本','华硕','2799',default,default);
insert into goods values(0,'x240 超级本','笔记本','联想','4880',default,default);
insert into goods values(0,'u330p 13.3寸笔记本','笔记本','联想','4299',default,default);
insert into goods values(0,'svvp13226 触控超级本','超级本','索尼','7999',default,default);
insert into goods values(0,'ipad air 9.7平板电脑','平板电脑','苹果','3388',default,default);
insert into goods values(0,'ipad mini retina屏','平板电脑','苹果','2788',default,default);
insert into goods values(0,'ideacentre c340 20寸一体机','台式机','联想','3499',default,default);
insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔','2899',default,default);
insert into goods values(0,'benteng 服务器','服务器','戴尔','12899',0,0);
# 验证bit类型值是否正确
select is_show +1 from goods;
# 查询
select name,price from goods where cate_name = "超级本";
# 查询并以cate_name分组显示组内的商品name
select cate_name ,group_concat(name) from goods group by cate_name;
# 查询每种类别笔记本的平均价格
select cate_name ,avg(price) from goods group by cate_name;
# 查询每种类别价格最贵的笔记本的信息
select * from goods 
inner join(
select cate_name ,max(price) as max_price from goods group by cate_name) as goods_max
on goods.cate_name = goods_max.cate_name and goods.price = goods_max.max_price;

# 创建商品分类表
create table if not EXISTS goods_cates(
    id int unsigned PRIMARY KEY auto_increment,
    name varchar(40) not null
);
# 插入数据
insert into goods_cates (name) values ("路由器"),("网卡"),("交换机");
# 将商品表中的分类写入到分类表中goods_cates，因为后面的值是多列的，所以不能加values
insert into goods_cates (name) select cate_name from goods group by cate_name;
# 使用商品分类表中的id替换掉商品表中的cate_name 
update goods inner join goods_cates on goods.cate_name=goods_cates.name  
set goods.cate_name = goods_cates.id ;
# 修改关联字段数据类型相同
alter table goods change cate_name cate_id int unsigned not null;
# 增加外键控制
alter table goods add FOREIGN KEY (cate_id) REFERENCES goods_cates(id);
# 插入不存在cate_id的数据失败
# insert into goods values(0,'benteng 服务器',11,'戴尔','12899',0,0);
# 创建商品品牌表brand_name ，并直接写入数据
create table if not exists goods_brand(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
) select brand_name as name from goods GROUP BY brand_name;
# 修改表名
alter table goods_brand rename to goods_brands;
# 更新商品表中的brand_name数据
update goods as g inner join goods_brands on g.brand_name=goods_brands.name set g.brand_name=goods_brands.id;
# 修改字段数据结构
alter table goods change brand_name brand_id int unsigned not null ;
# 增加外键控制
alter table goods add FOREIGN KEY (brand_id) REFERENCES goods_brands(id);
# 查看创建表语句
show create table goods;
# 实际开发工作中很少用到外键，因为降低开表的查询效率。删除外键
alter table goods drop FOREIGN KEY goods_ibfk_1;
alter table goods drop FOREIGN KEY goods_ibfk_2;

# sql注入：
select * from goods where name = " ";
select * from goods where name = "   " or 1=1 or "1    "; 

# 创建视图（虚拟的表格）
create view v_goods_info as select g.*,c.name as cate_name,b.name as brand_name from goods as g left join goods_cates as c on g.cate_id =c.id left join goods_brands as b on g.brand_id =b.id;

# 删除视图
drop view v_goods_info;
# 视图的作用
## 提高了重用性，就像一个函数一样
## 对数据库重构，却不影响程序的运行（什么时候查询视图，什么时候重新执行视图创建的语句）
## 提高了安全性能，可以对不同的用户
## 让数据更加清晰（简化查询语句，相当把原始查询语句封装了）

# 事务：有些任务必须同时操作多个表，这几个表必须同时操作完成才可以，比如记账，如果只有一个科目记账成功、另一个记账不成功，那么就会出问题。
# 事务的四大特性：
## 原子性：一个事务必须视为一个不可分的最小单元，整个事务要么全部成功，要么全部回滚。不可能只执行其中的一部分。
## 一致性：数据库从一个一致性的状态转换到另一个一致性的状态。
## 隔离性：可以理解为阻塞，当一个事务未执行完成，有其他程序对该表进行修改时，会将其他程序挂机。
## 持久性: 一旦事务提交，则其所做的修改会永久保存到数据库中。
# 开始一个事务
start transaction; # 或 begin;
select ...
update ...
update ...
COMMIT; 
