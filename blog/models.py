from django.db import models

#create model
class  Blog(models.Model):
	title  = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()
	body = models.TextField( )
	image = models.ImageField(upload_to='images/')

#add blog app to settings

#create migration

#migrate

#add to admin