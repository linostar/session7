from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
	firstname = models.CharField(max_length=100, db_index=True)
	lastname = models.CharField(max_length=100)
	age = models.FloatField()
	user = models.ForeignKey(User, null=True, blank=True, db_index=True)

	def __str__(self):
		return "{} {}".format(self.firstname, self.lastname)


class Post(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(null=True, blank=True)
	visible = models.BooleanField(default=True)
	creationdate = models.DateTimeField(default=datetime.now, db_index=True)
	author = models.ForeignKey(Author, null=True, blank=True, db_index=True)




