from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Author(models.Model):
	salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=40)
	email = models.EmailField()
	headshot = models.ImageField(upload_to='/tmp')

class Books(models.Model):
	title = models.CharField(max_length=130)
	authours = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
		

# Create your models here.
