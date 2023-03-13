from django.urls import path
from .views import HomeView, AddMovieView, SearchResultsListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('add_movie/', AddMovieView.as_view(), name='add_movie'),
	path("search/", SearchResultsListView.as_view(),name="search_results"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)