from django.db import models


class Post(models.Model):
	tag = models.CharField(max_length=20)
	image = models.ImageField(upload_to='photos')