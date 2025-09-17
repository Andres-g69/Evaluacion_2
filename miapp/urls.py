from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publicacion', views.publicacion, name='publicacion'),
    path('ranking', views.ranking, name='ranking'),
]