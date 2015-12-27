drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  job string not null
);