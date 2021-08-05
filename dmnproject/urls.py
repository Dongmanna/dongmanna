# dmnproject/urls.py
from django.contrib import admin
from django.urls import path, include
from main import views
import accounts.views
# for uploading media files
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('detail/<int:pk>/delete', views.delete, name="delete"),
    path('search/', views.SearchFormView.as_view(), name='search'),

    path('accounts/', include('accounts.urls')),
]

# for uploading media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)