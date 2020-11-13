from django.db import models

# Create your models here.
from django.db import models


class Game(models.Model):
	name = models.CharField(help_text='游戏名称', default='', max_length=50)
	pinyin_name = models.CharField(help_text='游戏拼音名', default='', max_length=50)
	pinyin_first = models.CharField(help_text='游戏拼音首字母', default='', max_length=50)
	en_name = models.CharField(help_text='游戏英文名', default='', max_length=50)
	other_name = models.CharField(help_text='游戏别名', default='', max_length=200)
	title_img = models.CharField(help_text='游戏题图', default='', max_length=200)
	icon = models.CharField(help_text='游戏题图', default='', max_length=200)
	introduce = models.TextField(help_text='游戏简介', default='', max_length=200)
	uid = models.IntegerField(help_text='用户id', default=0)
	platform = models.CharField(help_text='游戏平台 1=PC, 2=移动端, 3=XBOX, 4=PS, 5=NS', default='', max_length=20)
	state = models.IntegerField(help_text='游戏题图', default='')
	create_time = models.IntegerField(help_text='创建时间', default=0)
	update_time = models.IntegerField(help_text='更新时间', default=0)
	wiki = models.CharField(help_text='游戏wiki', default='', max_length=200)
	publish_date = models.IntegerField(help_text='发售日期', default=0)
	other_info = models.CharField(help_text='游戏其他信息', default='', max_length=2000)
	game_shot = models.CharField(help_text='游戏截图', default='', max_length=2000)
	game_video = models.CharField(help_text='游戏视频', default='', max_length=2000)
	review_count = models.IntegerField(help_text='游戏点评总数', default=0)
	user_grade = models.IntegerField(help_text='用户总评分', default=0)
	admin_grade = models.IntegerField(help_text='官方总评分', default=0)
	user_grade_num = models.IntegerField(help_text='用户评分人数', default=0)

	def __repr__(self):
		return "Game:{id:%s, name:%s}" % (self.id, self.name)

	def Save(self):
		info = {}
		info["id"] = self.id
		info["name"] = self.name
		info["pinyin_name"] = self.pinyin_name
		info["pinyin_first"] = self.pinyin_first
		info["en_name"] = self.en_name
		info["other_name"] = self.other_name
		info["title_img"] = self.title_img
		info["icon"] = self.icon
		info["introduce"] = self.introduce
		info["uid"] = self.uid
		info["platform"] = self.platform
		info["state"] = self.state
		info["create_time"] = self.create_time
		info["update_time"] = self.update_time
		info["wiki"] = self.wiki
		info["publish_date"] = self.publish_date
		info["user_grade"] = self.user_grade
		info["admin_grade"] = self.admin_grade
		info["user_grade_num"] = self.user_grade_num
		info["other_info"] = self.other_info
		info["game_shot"] = self.game_shot
		info["game_video"] = self.game_video
		info["review_count"] = self.review_count

		return info

	class Meta:
		db_table = "game"


class GameBoard(models.Model):
	gid = models.IntegerField(help_text="游戏id", default=0)
	bid = models.IntegerField(help_text="榜单id", default=0)
	ct = models.IntegerField(help_text='创建时间', default=0)

	def __repr__(self):
		return "<GameBoard(gid:%s bid:%s)>" % (self.gid, self.bid)

	class Meta:
		db_table = "tbl_game_board"


class Board(models.Model):
	name = models.CharField(help_text='榜单名称', default='', max_length=30)
	introduce = models.CharField(help_text='榜单简介', default='', max_length=500)
	title_img = models.CharField(help_text='榜单题图', default='', max_length=50)
	type = models.IntegerField(help_text='榜单类型, 客户端显示使用', default=0)
	ct = models.IntegerField(help_text='创建时间', default=0)
	ut = models.IntegerField(help_text='更新时间', default=0)

	def __repr__(self):
		return "<Board(name:%s type:%s)>" % (self.name, self.type)

	class Meta:
		db_table = "tbl_board"