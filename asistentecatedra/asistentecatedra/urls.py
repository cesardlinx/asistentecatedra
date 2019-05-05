from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('asistente.urls')),
    path('accounts/', include('accounts.urls')),
    path('planificaciones/', include('planificaciones.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
