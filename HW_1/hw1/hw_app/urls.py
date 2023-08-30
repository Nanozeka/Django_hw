from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='Main'),
    path('about/', views.about, name='About'),
]