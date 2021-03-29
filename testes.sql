create table if not exists cursos(
nome varchar(30) not null unique,
descricao text,
carga int unsigned,
totaulas int,
ano year default '2021'
) default charset = utf8;

alter table cursos
add idcurso int first;

alter table cursos
add primary key(idcurso);

alter table cursos
modify idcurso int auto_increment;

alter table cursos
change idcurso id int auto_increment;

rename table galera to alunos;


desc cursos;

insert into cursos
values
(default,'Historia do Brasil', 'O curso trata sobre pontos significativos da historia nacional', '80', '40',default);

insert into cursos
values
(default,'HTML4','Curso de HTML5','40','37','2014'),
(default,'Cozinha Árabe','Aprenda a fazer Kibe','40','30','2016'),
(default,'Youtuber','Gerar polêmica e ganhar inscritos','40','30','2018'),
(default,'Word','Curso completo de Word','40','30','2016'),
(default,'Sapateado','Danças Rítmicas','40','30','2018');

use cadastro;

select*from cursos;  
select*from alunos;

update cursos
set nome = 'HTML5'
where id = '4';

update cursos
set nome = 'PHP', ano = '2015'
where id = '2';

update cursos
set nome =  'Java', ano = '2014', carga = '30'
where id = '3'
limit 1;

delete from cursos
where id = '8';

/*truncate table nome_da_coluna 
drop database nome_do_bd */



