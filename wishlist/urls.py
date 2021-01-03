from django.urls import path
from . import views

urlpatterns = [
    path('add_wish/', views.add_wish, name='add_wish'),
    path('update_wish/<str:pk>', views.update_wish, name='update_wish'),
    path('delete_wish/<str:pk>', views.delete_wish, name='delete_wish')
]
