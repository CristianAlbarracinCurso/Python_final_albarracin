from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Administración
    path('admin/', admin.site.urls),

    # Blog
    path('', include('blog.urls')),  

    # Cuentas y autenticación
    path('accounts/', include('allauth.urls')),  

    # Mensajería
    path('messaging/', include('messaging.urls')),  
]

# Manejo de archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


