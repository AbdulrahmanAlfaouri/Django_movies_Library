from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'year', 'my_rating', 'movie_type']

admin.site.register(Movie, MovieAdmin)