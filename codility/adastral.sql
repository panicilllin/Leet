select     *  from tab a where  exists(
select id from (
        select id, row_number() over(partition by city oder by id ) rn  from tab
 ) tab where rn < 51 and  a.id= tab.id )



SELECT f.id,f.city,f.price FROM (
    SELECT id,city,price,row_number() OVER(partition by city order by price desc) as n
    FROM flats) f
    WHERE f.n <=3;