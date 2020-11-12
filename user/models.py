from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):

	name = models.CharField(max_length=50)

	def __repr__(self):
		return "User:{id:%s, name:%s}" % (self.id, self.name)

	class Meta:
		db_table = "user"
		ordering = ['name']