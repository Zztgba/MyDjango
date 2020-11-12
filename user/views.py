from django.shortcuts import render

# Create your views here.
# !/usr/bin/env/python
# _*_coding:utf-8_*_
import json

from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Count

import user.models


# insert
def insert(request):
	test1 = user.models.User(name='test1')
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")


# select
def get(request):
	response1 = []
	model = user.models.User
	# 只需要返回部分字段
	games = model.objects.values("id", "name").filter(id=1).distinct()

	# 全表查
	list = model.objects.all()
	# where条件查询:
	var_temp = model.objects.filter(id=1, name="test1")
	var2 = model.objects.filter(Q(name="test1") | Q(name="test2"))
	# 范围条件
	model.objects.filter(id__in=[1, 2, 3])  # in
	model.objects.filter(id__range=[1, 3])  # 1<=id<=3
	model.objects.filter(id__gt=1)  # id>1   id__gte=1   id>=1
	model.objects.filter(id__lt=3)  # id<3   id__lte=3   id<=3
	# 模糊搜索
	model.objects.filter(name__contains="t")  # 区分大小写
	model.objects.filter(name__icontains="T")  # 不区分大小写
	model.objects.filter(name__startswith="t")
	model.objects.filter(name__endswith="t")
	# order_by
	model.objects.order_by("id")  # 升序
	model.objects.order_by("-id")  # 降序
	# count函数 exists函数
	model.objects.filter(name__contains="e").count()  # 查询符合规则的数据数量
	temp = model.objects.filter(name__contains="s").exists()
	# group by
	temp = model.objects.values("id", "name").values("name").annotate(Count=Count("name")).order_by("name")
	list6 = model.objects.filter(name="test1").order_by("id")

	# 原生sql查询
	# temp = model.objects.raw("select id, name from user where name = %s", ["test1"])
	# for user in temp:
	# 	id = user.id
	# 	name = user.name

	for _game in list:
		response1.append({
			"id": _game.id,
			"name": _game.name
		})

	return HttpResponse(json.dumps(response1))


def update(request):
	# 方法一、推荐用法,会返回整数(更新行数
	res = user.models.User.objects.filter(name="test1").update(name="test999")

	# 方法二、
	# game = user.models.User.objects.filter(id=1).first()
	# game.name = "123"
	# game.save()
	return HttpResponse("ok")


def delete(request):
	user1 = user.models.User.objects.get(name='test1')
	user1.delete()
	return HttpResponse("ok")
