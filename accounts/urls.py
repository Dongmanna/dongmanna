# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
]