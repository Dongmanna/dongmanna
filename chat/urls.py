# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:room_number>', views.room, name='room'),
    path('newRoom/<int:pk>', views.newRoom, name='newRoom'),
    path('checkRoom/', views.checkRoom, name='checkRoom'),
    path('send/', views.send, name='send'),
    path('getMessages/<int:room_number>', views.getMessages, name='getMessages'),
]