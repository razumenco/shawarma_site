from django.urls import path
from . import views

urlpatterns = [
    path('',
        views.shawarma_list,
        name='shawarma_list'),
    path('<int:id>/',
        views.shawarma_detail,
        name='shawarma_detail'),
    path('about',
         views.about,
         name='about')
]