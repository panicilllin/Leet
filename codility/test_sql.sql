
Create table If Not Exists Activity (user_id int, device_id int, event_date date, videos_watched int)
Truncate table Activity
insert into Activity (user_id, device_id, event_date, videos_watched) values ('1', '2', '2016-03-01', '5')
insert into Activity (user_id, device_id, event_date, videos_watched) values ('1', '2', '2016-03-02', '6')
insert into Activity (user_id, device_id, event_date, videos_watched) values ('2', '3', '2017-06-25', '1')
insert into Activity (user_id, device_id, event_date, videos_watched) values ('3', '1', '2016-03-02', '0')
insert into Activity (user_id, device_id, event_date, videos_watched) values ('3', '4', '2018-07-03', '5')
# table


select user_id from
    {select user_id, event_date from Activity Group by user_id order by event_date limit 2} as a
where (a.event_date - a.event_date_2 < 1d);





select name, id from users

users_list = users.id().all()
user_val_dict={}
for user in user_list:
    user_val_dict[user] = valuation(user_id=users.id)


with
select name, count(*) from valuation
                      group by user_id
                      join user
                      on user_id=user.id


