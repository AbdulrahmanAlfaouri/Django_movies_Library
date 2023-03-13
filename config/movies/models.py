from django.db import models

class Movie(models.Model):
	
	class MyRating(models.IntegerChoices):
		one = 1
		tow = 2
		three = 3
		four = 4
		five = 5

	class Types(models.TextChoices):
		action = 'action'
		drama = 'drama'
		family = 'family'
		animations = 'animations'

	

	name = models.CharField(max_length=100)
	movie_type = models.CharField(max_length=10,choices=Types.choices)
	my_rating = models.IntegerField(default=0, choices=MyRating.choices)
	description = models.TextField(default='None')
	year = models.DateField()
	length = models.DurationField(default='1:00:00')
	image = models.ImageField(upload_to='images/',default='images/1.jpg', null=True)


	def __str__(self):
		return self.name
