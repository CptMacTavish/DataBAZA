drop table if exists entries;
create table entries (
  id serial primary key not null,
  date timestamp with time zone not null default now(),
  title varchar(80) not null,
  content text not null
);
INSERT INTO entries values(1, default, 'About nothing', 'This is flask app was written by Matkovskyi Stanislav'),
(2, default, 'About thing', 'This is flask app was written by flask app'),
(3, default, 'About ing', 'This is flask app was written by hands'),
(4, default, 'About no', 'This is flask app was written by BAZA'),
(5, default, 'About no', 'This is flask app was written by BAZA AZOVA'),
(6, default, 'About no', 'This is flask app was written by Matkovskyi SS');