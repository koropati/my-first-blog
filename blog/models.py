from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	"""docstring for Post"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Jurnal(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	judul = models.CharField(max_length=500)
	penulis = models.CharField(max_length=200)
	tahun = models.DateField(blank=True, null=True)
	sensor = models.CharField(max_length=500)
	algoritma = models.TextField()
	penerapan = models.CharField(max_length=500, null=True)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.judul

class Data(models.Model):
	"""docstring for Data"""
	created_date = models.DateTimeField(default=timezone.now)
	data = models.TextField()

	def publish(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.created_date
		
		