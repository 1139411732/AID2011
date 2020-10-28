 create table class_1 (id int primary key auto_increment
 ,name varchar(50) not null,age tinyint unsigned ,
 sex enum('m','w','o'),
 score float default 0);


insert into class_1 values
(1,'戴乐成','3','o',1),
(2,'小戴乐成','33','w',10),
(3,'中戴乐成','22','m',12),
(4,'大戴乐成','15','o',13);

insert into class_1
(name,age,sex) values
('大聪明',17,'w');

insert into class_1
(name,age,score) values
('戴乐成的爸爸',20,60);

--#------------

create table hobby_1 (id int primary key auto_increment,
name varchar(50) not null,
hobby set('dance','sing','draw'),
level enum('A','B','C','D') comment '初始评级',
price decimal(7,2),
remark varchar(600) comment '备注信息');


insert into hobby_1 values
(1,'戴乐成','dance,sing','A',12345.08,'是凌晨的孙子'),
(2,'小戴乐成','draw,sing','B',54321.00,'同上面的'),
(3,'中戴乐成','dance,draw','C',125.08,'同上上面的');


insert into hobby_1 (name,hobby,level,price)values
('武大郎','dance,sing','A',12345.08);










