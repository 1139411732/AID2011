create table sanguo(
id int primary key auto_increment,
name varchar(30),
gender enum('男','女'),
country enum('魏','蜀','吴'),
attack smallint,
defense tinyint
);
insert into sanguo
values (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 377, 66),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 303, 60),
       (13, '吕蒙', '男', '吴', 330, 71);
--1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country = '蜀'
order by attack;
--2. 将赵云攻击力设置为360，防御设置为70
update sanguo set attack = 360,defense = 70
where name = '赵云';
--3. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo set attack = 300 where country =
'吴' and attack>300 limit 2;
--4. 查找攻击力超过200的魏国英雄名字和攻击力并显示为姓名,攻击力

