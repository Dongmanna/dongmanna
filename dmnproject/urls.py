# dmnproject/urls.py
from django.contrib import admin
from django.urls import path, include
# for uploading media files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
]

# for uploading media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)