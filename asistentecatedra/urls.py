from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('', include('asistente.urls')),
    path('accounts/', include('accounts.urls')),
    path('planificaciones/', include('planificaciones.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/upload/', ckeditor_views.upload,
         name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(ckeditor_views.browse),
         name='ckeditor_browse'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'asistente.views.handler404'
handler500 = 'asistente.views.handler500'
