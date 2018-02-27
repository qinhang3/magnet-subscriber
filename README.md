# magnet-subscriber
学习python的小玩具
订阅根据关键字订阅BT磁力链
前端：vue+element ui+axio
后端：python+Flask RESTful+sqlite

#Run
```
sudo pip install HTMLParser
sudo pip install flask
sudo pip install flask-restful
sudo python web.py
```

#init database
```
create table task
(
	keyword,
	magnet,
	gmt_create,
	gmt_modified,
	delete_mark
)
;

create table torr
(
	keyword,
	sup,
	title,
	detail,
	attr,
	magnet,
	gmt_create,
	delete_mark
)
;
```
