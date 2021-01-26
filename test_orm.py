#!/usr/bin/env/python
#_*_coding:utf-8_*_
# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
测试接口
"""

import requests
import time




for j in range(3):
	start = time.time()
	sql_exe = []
	for i in range(1000):
		i = i % 10
		response = requests.get("http://127.0.0.1:8000/game/all?param=%s" % i)
		sql_exe.append(float(response.text))

	sql_time = 0
	for i in sql_exe:
		sql_time += i
	end = time.time()

	print("%s   cost_time:%.2f  sql_time:%.2f" % (j+1, end-start, sql_time))



"""
1000次请求耗时情况
cost_time 总耗时
sql_time 服务端sql执行总耗时
连接池
1   cost_time:8.41  sql_time:2.16
2   cost_time:8.27  sql_time:2.18
3   cost_time:7.96  sql_time:2.20


无连接池
1   cost_time:8.63  sql_time:2.69
2   cost_time:8.84  sql_time:2.82
3   cost_time:8.45  sql_time:2.69

结论
由于Django的ORM对数据库操作结果为QuerySet，在QuerySet查询提交之前，不会发生任何实际数据库操作。
顾sql_time字段反应的数据为 获取数据库连接+数据库操作 总时间
Django 采用连接池方式能稍微提升获取数据库连接的开销

相对于SQLAlchemy,
Django的ORM框架效率较低，但其模型映射联系更为紧密，并可通过Model反向生成数据库表。
"""