from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('asistente.urls')),
    path('accounts/', include('accounts.urls')),
    path('planificaciones/', include('planificaciones.urls')),
    path('admin/', admin.site.urls),
]

if settings.DJANGO_ENV == 'development':
    urlpatterns = [
        path('', include('asistente.urls')),
        path('accounts/', include('accounts.urls')),
        path('planificaciones/', include('planificaciones.urls')),
        path('admin/', admin.site.urls),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'asistente.views.handler404'
handler500 = 'asistente.views.handler500'
