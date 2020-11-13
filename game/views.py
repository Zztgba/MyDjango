from django.shortcuts import render
from django.http import HttpResponse

import game.models
import time
import xpinyin
import json

def insert_game(request):
	if request.method == "POST" and request.POST:
		True
	curtime = int(time.time())
	pinyin = xpinyin.Pinyin()
	request = json.loads(request.body)
	name = request.get("name")
	test1 = game.models.Game(
			name=name,
			pinyin_name=pinyin.get_pinyin(name, ""),
			pinyin_first=pinyin.get_initials(name, ""),
			en_name=request.get("enname", pinyin.get_pinyin(name, "")),
			other_name=request.get("othername", ""),
			title_img=request.get("special", ""),
			icon=request.get("icon", ""),
			introduce=request.get("introduce", ""),
			uid=0,
			platform=",".join(str(i) for i in request.get("gameplatform", [])),
			wiki=request.get("wiki", ""),
			state=0,
			create_time=curtime,
			update_time=curtime,
			publish_date=request.get("publishdate", 0),
			other_info=json.dumps(request.get("otherInfo", "")),
			game_shot=json.dumps(request.get("gameShot", [])),
			game_video=json.dumps(request.get("gameVideo", [])),
	)
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")

def insert_board(request):
	request = json.loads(request.body)
	curtime = int(time.time())
	test1 = game.models.Board(
			name=request.get("name"),
			introduce=request.get("introduce", ""),
			title_img=request.get("title_img", ""),
			type=request.get("type"),
			ct=curtime,
			ut=curtime,)
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")


def all_games(request):
	i = request.GET.get("param")
	start = time.time()
	sql_res = game.models.Game.objects.filter(name__icontains=i)
	response1 = []
	for _game in sql_res:
		response1.append(_game.Save())
	end = time.time()
	cost_time = end - start
	return HttpResponse(cost_time)