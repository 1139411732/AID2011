--视图创建
create view good_student as
select name,age,score from cls where score >=10;
--查看stu库中共存那些视图
show full tables in stu where table_type like 'view';

--自定义函数

delimiter $$

create function st() returns int
begin
return (select score from cls order by score desc limit 1);
end $$

delimiter ;


delimiter $$
--函数
create function st2() returns int
begin
declare a int;
declare b int;
set a = (select score from cls order by score desc limit 1);
select score from cls order by score  limit 1 into b;
return a-b;
end $$
delimiter ;

delimiter $$
create function queryNameById(uid int)
returns varchar(20)
begin
return  (select name from class_1 where id=uid);
end $$

delimiter ;

create procedure st()
begin
select name ,age from cls;
delete from cls where score < 0;
select score from cls order by score desc limit 1;
end $$
call st() -- 要用call调用

set @a=100;
select @a
--存储过程
create procedure p_in(in num int)
begin
select num;
set num = 100;
select num;
end $$

--查看函数信息
show function status like 'st';
--查看函数的定义方法
show create procedure st ;
--查看库中的函数或者是存储过程
select name from mysql.proc
where db='stu' and type='[procedure/function]';
--删除存储过程或存储函数
drop {procedure | function} [IF EXISTS] sp_name;

练习:
--1. 编写一个函数,传入两个同学的ID值,返回两位同学
create function st1(c int,d int)
returns float
begin
declare a float;
declare b float;
select score from cls where id=c into a;
select score from cls where id=d into b;
return a-b;
end $$
--函数用 select 调用

--2. 编写一个存储过程, 通过用户变量传入学生的姓名
--,使用该用户变量得到这个学生的成绩
create procedure get_score(inout stu varchar(30))
begin
set stu=(select score from cls where name=stu);
end $$

set @name="Lily";
call get_score(@name);
select @name;



