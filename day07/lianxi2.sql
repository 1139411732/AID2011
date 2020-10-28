create database relation charset =utf8;
create table student (id int primary key auto_increment,name varchar(50) not null);

create table record (id int primary key auto_increment,comment text not null,
st_id int unique,
constraint st_fk foreign key (st_id) references student(id)
on delete cascade
on update cascade
);



create database weixin relation charset=utf8

--用户表
create table user(
id int primary key auto_increment,
name varchar(30) not null,
passwd char(64),
tel char(16)
);

--朋友圈表
create table pyq(
id int primary key auto_increment,
image blob,
content text,
time datetime,
u_id int comment "关系字段",
foreign key (u_id) references user(id)
);

--点赞评论
create table like_talk(
id int primary key auto_increment,
uid int,
pid int,
`like` bit,
talk text,
foreign key (uid) references user(id),
foreign key (pid) references pyq(id)
);

