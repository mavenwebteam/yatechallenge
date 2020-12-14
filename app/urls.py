from django.urls import path
from .import views 

urlpatterns = [
	path('genres', views.show_genres, name='show_genres'),
]