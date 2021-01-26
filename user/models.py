from django.db import models

# Create your models here.
from django.db import models

class UserSplit(models.Model):

	__abstract__ = True

	uid = models.IntegerField()
	ct = models.IntegerField()

	class Meta:
		abstract = True


def get_model(split):
	split = split % 3

	class Meta:
		db_table = 'user_%s' % split

	attrs = {
		'__module__': UserSplit.__module__,
		'Meta': Meta
	}
	return type(str('User_%s' % split), (UserSplit,), attrs)