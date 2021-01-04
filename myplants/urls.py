from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get_locations/', views.get_locations, name='get_locations'),
    path('get_plants_by_user/<str:pk>', views.get_plants_by_user, name='get_plants_by_user'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('update_plant/<str:pk>', views.update_plant, name='update_plant'),
    path('delete_plant/<str:pk>', views.delete_plant, name='delete_plant'),
    path('other_user/<str:pk>', views.other_user, name='other_user')
]
