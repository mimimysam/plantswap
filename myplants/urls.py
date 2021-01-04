from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('update_plant/<str:pk>', views.update_plant, name='update_plant'),
    path('delete_plant/<str:pk>', views.delete_plant, name='delete_plant')
]
