from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Administración
    path('admin/', admin.site.urls),

    # Blog
    path('', include('blog.urls')),  # Incluye las rutas del blog (posts, páginas, etc.)

    # Cuentas y autenticación
    path('accounts/', include('allauth.urls')),  # Rutas para registro, login y más con django-allauth

    # Mensajería
    path('messaging/', include('messaging.urls')),  # Funcionalidad de mensajería entre usuarios
]

# Manejo de archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# En producción, configurar un servidor para manejar estáticos/medios
