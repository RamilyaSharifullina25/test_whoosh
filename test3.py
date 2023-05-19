# Я развернула СУБД psql на своем локальном компьютере, далее команды для выполнения задания:

# создадим таблицу test_whoosh
create table test_whoosh (
x timestamp NOT NULL,
id integer NOT NULL,
scooters_on_parking integer NOT NULL,
timezone text NOT NULL); 

# скопируем данные из csv в таблицу
copy test_whoosh from '/Users/ramilasarifullina/Desktop/test_whoosh/test_table_final.csv' with (format csv, header true);

# группировка записей по 3 часа и id пространственных точек и начальное количества самокатов в этот временной промежуток
with adt2 as (with adt as (select id, x, scooters_on_parking, div(extract('hour' from x), 3) as div from test_whoosh where x!= '2022-06-02 00:00:00' order by id, x) select adt.id, adt.x, adt.scooters_on_parking, adt.div, row_number() over(partition by id, div) as first_row from adt) select adt2.x, adt2.id, adt2.scooters_on_parking from adt2 where first_row=1;

# добавим колонку last_scooter_on_parking, где будем считать кол-во самокатов на паркинге в предыдущие пол часа
select *, lag(scooters_on_parking) over(partition by id order by x asc) as last_scooter_on_parking from test_whoosh order by id;

# приведение времени к нужной timezone

# инкрментальное обновление данных

