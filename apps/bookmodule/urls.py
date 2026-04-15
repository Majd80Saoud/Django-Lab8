from django.urls import path
from . import views



urlpatterns = [
   
    path('', views.index, name='index'),
    path('list/', views.list_books, name='list_books'),
    path('about/', views.aboutus, name='aboutus'),

    path('html5/lab5/', views.lab5, name='lab5'),

    path('search/', views.search, name='search'),

    path('simple/query', views.simple_query, name='simple_query'),

     path('complex/query', views.complex_query, name='complex_query'),

     path('lab8/task1', views.lab8_task1, name='lab8_task1'),

     path('lab8/task2', views.lab8_task2, name='lab8_task2'),

     path('lab8/task3', views.lab8_task3, name='lab8_task3'),

     path('lab8/task4', views.lab8_task4, name='lab8_task4'),

     path('lab8/task5', views.lab8_task5, name='lab8_task5'),

     path('lab8/task7', views.lab8_task7, name='lab8_task7'),
   
]