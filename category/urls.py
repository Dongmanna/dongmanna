from django.urls import path
from . import views

urlpatterns = [
    path('offline_category/',views.offline_category , name='offline_category'),
    path('online_category/',views.online_category , name='online_category'),
    path('delivery_category/',views.delivery_category , name='delivery_category'),
    path('search_on/', views.SearchFormView_on.as_view(), name="search_on"),
    path('search_of/', views.SearchFormView_of.as_view(), name="search_of"),
    path('search_de/', views.SearchFormView_de.as_view(), name="search_de"),

]