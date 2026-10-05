-- distinct city
-- select count(distinct lat, lon) from Insurance
-- select lat, lon, count(*), from Insurance group by lat, lon,
-- select *, count(*) as city from Insurance group by lat, lon 
with a as (
    select i.tiv_2015 , count(i.tiv_2015) as 2k15 from Insurance as i group by i.tiv_2015
),
b as (
select tiv_2015 from  a where a.2k15>1
),
c as(
select pid,lat,lon, count(*) as city from Insurance as i  group by i.lat, i.lon
),
d as(
select pid from c where c.city=1
)
select ROUND(sum(i.tiv_2016), 2) as tiv_2016 from Insurance i, b, d
where i.pid=d.pid and i.tiv_2015=b.tiv_2015;



select ROUND(SUM(DISTINCT i1.tiv_2016),2) as tiv_2016 
from Insurance i1, Insurance i2
where i1.tiv_2015 = i2.tiv_2015
  AND i1.pid <> i2.pid 
  AND i1.pid NOT IN 
    (select DISTINCT a.pid 
    from insurance a, insurance b
    where  a.pid <> b.pid 
       AND a.lat = b.lat 
       AND b.lon = a.lon
    );