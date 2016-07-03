from __future__ import unicode_literals

from django.db import models


class events(models.Model):
	event_type=models.CharField(max_length=3,choices=(('tech','Techinical'),('art','Art'),('sports','Sports'),('cultural','Custoral')),help_text="haii this is help")
	pic=models.BinaryField()
	is_college=models.BooleanField()
	date_reg=models.DateField(auto_now=True)

	budget=models.DecimalField(decimal_places=4,max_digits=5	)
	duration=models.DurationField()
	email=models.EmailField()
	#document=models.FileField(upload_to="uploads/")

	#image=models.ImageField()
	ip=models.GenericIPAddressField()


# Create your models here.
