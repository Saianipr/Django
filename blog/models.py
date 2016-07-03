from __future__ import unicode_literals

from django.db import models


class post(models.Model):
	name=models.CharField(max_length=120)
	body=models.TextField()
	date=models.DateTimeField()


# Create your models here.
