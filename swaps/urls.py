from django.urls import path
from . import views

urlpatterns = [
    path('swaps/', views.search_plants, name='search_plants'),
]
