--创建
create table dept (id int primary key auto_increment,dname varchar(50) not null);
insert into dept values
(1,'技术部'),
(2,'生产部'),
(3,'研发部');
--插入
create table person (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(32) NOT NULL,
  age tinyint DEFAULT 0,
  sex enum('m','w','o') DEFAULT 'o',
  salary decimal(8,2) DEFAULT 250.00,
  hire_date date NOT NULL,
  dept_id int
);

insert into person values (1,'戴乐成',26,'m',15000,'2019-5-3',1);
insert into person values (2,'凌晨',26,'m',15000,'2019-5-3',2);
insert into person values (3,'大朗',26,'m',15000,'2019-5-3',3);
--添加外键并关联字段
alter table person add constraint dept_fk foreign key(dept_id) references dept(id);
--查看外键表信息
show create table person;
--删除外键
alter table person drop foreign key dept_fk;
alter table person drop foreign key person_ibfk_1;
--删除外键索引
alter table person drop index dept_id;
--第一种 级联动作 添加外键并关联字段且约束级联动作
alter table person add foreign key (dept_id)
references dept(id)
on delete cascade on update cascade;
--第二种 级联动作
alter table person add foreign key (dept_id)
references dept(id)
on delete set null    on update set null
--修改字段内容
update dept set id=4 where dname = '研发部';




create table class(cid int primary key auto_increment,
                  caption char(4) not null);

create table teacher(tid int primary key auto_increment,
                    tname varchar(32) not null);

create table student(sid int primary key auto_increment,
                    sname varchar(32) not null,
                    gender enum('male','female','others') not null default 'male',
                    class_id int,
                    foreign key(class_id) references class(cid)
                    on update cascade
                    on delete cascade);

create table course(cid int primary key auto_increment,
                   cname varchar(16) not null,
                   teacher_id int,
                   foreign key(teacher_id) references teacher(tid)
                   on update cascade
                   on delete cascade);

create table score(sid int primary key auto_increment,
                  student_id int,
                  course_id int,
                  number int(3) not null,
                  foreign key(student_id) references student(sid)
                   on update cascade
                   on delete cascade,
                   foreign key(course_id) references course(cid)
                   on update cascade
                   on delete cascade);


insert into class(caption) values('三年二班'),('三年三班'),('三年一班');
insert into teacher(tname) values('波多老师'),('苍老师'),('小泽老师');
insert into student(sname,gender,class_id) values('钢蛋','female',1),('铁锤','female',1),('山炮','male',2),('彪哥','male',3);
insert into course(cname,teacher_id) values('生物',1),('体育',1),('物理',2);
insert into score(student_id,course_id,number) values(1,1,60),(1,2,59),(2,2,100),(3,2,78),(4,3,66);

--1. 查询每位老师教授的课程数量
select teacher.tname,count(teacher_id)
from teacher left join course
on teacher.tid = course.teacher_id
group by tname;
--2. 查询学生的信息及学生所在班级信息
select student.sname,student.gender,class.caption
from student left join class
on student.class_id = class.cid;

--3. 查询各科成绩最高和最低的分数,形式 :
--课程ID  最高分  最低分
select score.course_id,max(score.number) as
最高分,min(score.number) as 最低分
from score left join course on course.cid = score.course_id
group by course_id;
--4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select sname,student.sid,avg(score.number)
from score left join student on score.student_id = student.sid
group by sname,student.sid
having avg(score.number)>85;
--5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select student_id,student.sname,number
from score left join student on student.sid = score.student_id
where course_id = 2 and number >80;
--6. 查询各个课程及相应的选修人数
select course.cname,count(course_id)
from score left join course on course.cid = score.course_id
group by cname;

















