from datetime import datetime

from django.db import models


class Author(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	age = models.FloatField()

	def __str__(self):
		return "{} {}".format(self.firstname, self.lastname)


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(null=True, blank=True)
	visible = models.BooleanField(default=True)
	creationdate = models.DateTimeField(default=datetime.now)
	author = models.ForeignKey(Author, null=True, blank=True)




