from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Movie
from django.db.models import Q
from django.core.paginator import Paginator


class HomeView(ListView):
	model = Movie
	template_name = 'movielist_light.html'
	context_object_name = 'movies'

class AddMovieView(CreateView):
	model = Movie
	template_name = 'add_movie2.html'
	fields = '__all__'

	success_url = reverse_lazy('home')

class SearchResultsListView(ListView):
	model = Movie
	template_name = "search_results.html"
	context_object_name = 'movies'

	def get_queryset(self): # new
		name =  self.request.GET.get("name")
		year = self.request.GET.get('year')
		mtype = self.request.GET.get('type')

		return Movie.objects.filter(
		name__icontains=name).filter(movie_type__icontains=mtype).filter(year__icontains=year)