--1.打开 mysql数据库  ； 打开/停止/重启服务：start/stop/restart
sudo service mysql start
--2.连接数据库
mysql -u root -p
--查看已有库
show databases;
--3.创建数据库 books为库名
create database books charset=utf8;
--4.切换库(使用库) books为库名
use books;
--查看当前所在库
select database();
--删除数据库
drop database test;
--5.创建表
create table book(id int primary key auto_increment,
book_name varchar(30) not null,
author varchar(30) comment '作者',
publishing varchar(30)  default '不知道',
price decimal(6.2),
remark text);
--查看数据表
show tables;
--6.查看表结构
desc book;
--7.插入数据
insert into book values
(1,'《三国演义》','黄贯中','中国文学',90,'三个臭皮匠顶个诸葛亮');
insert into book (book_name,author,publishing,price) values
('《水浒传》','黄家驹','人民教育',39),
('《红楼梦》','曹雪芹','机械工业',50),
('《西游记》','凌晨','天地一号',120),
('《十万个为什么》','带了成','蠢货大法',30);
insert into book values
(6,'《计算机心理学》','老舍','中国文学',100,'一心钻研计算机');
('《背影》','鲁迅','人民教育',80);
('《黑色杀手锏》','茅盾','杀猪刀',70);
--8.查看表中全部内容
select * from book;
--练习1. 查找30多元的图书
select book_name,price from book where price > 30;
--练习2. 查找人民教育出版社出版的图书　
select book_name,publishing from book where publishing = '人民教育';
--练习3. 查找老舍写的，中国文学出版社出版的图书
--select book_name,author,publishing from book where author = ' 老舍' and publishing = '中国文学';
select book_name,author,publishing from book where author = '老舍' and publishing = '中国文学';
--练习4. 查找备注不为空的图书
select book_name,remark from book where remark is not null;
--练习5. 查找价格超过６０元的图书，只看书名和价格
select book_name,price from book where price > 60;
--练习6. 查找鲁迅写的或者茅盾写的图书
select * from book where author = '鲁迅' or author = '茅盾';

2
select publishing,count(publishing) from book group by publishing ;

3
select count(distinct publishing) from book  publishing;
4
select price,avg(price) from book where price > 50 group by
order by avg(price) desc;

select publishing,avg(price) from book
group by price having max(price)>50
order by avg(price) desc;

select publishing_date,max(price),min(price) from book group bymax(price) min(price);

