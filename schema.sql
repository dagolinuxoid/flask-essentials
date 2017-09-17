DROP TABLE if exists hero_dashboard;
CREATE TABLE hero_dashboard (
    id integer primary key autoincrement,
    hero_name text not null,
    hero_descr text not null
);