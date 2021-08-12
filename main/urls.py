# main/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('home/<str:category>', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('detail/<int:pk>/delete', views.delete, name="delete"),
    path('search/', views.SearchFormView.as_view(), name="search"),
    path('participated/<int:pk>/', views.post_participated_toggle, name="post_participated_toggle"),
]