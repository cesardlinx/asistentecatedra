from django.urls import path
from .views.planificaciones_view import PlanificacionesTemplateView
from .views.plan_clase_views import (PlanClaseListView,
                                     plan_clase_create,
                                     plan_clase_update,
                                     PlanClaseDeleteView,
                                     PlanClaseDuplicateView,
                                     PlanClasePdfView)
from .views.plan_anual_views import (PlanAnualListView,
                                     PlanAnualCreateView,
                                     PlanAnualUpdateView,
                                     PlanAnualDeleteView,
                                     PlanAnualDuplicateView,
                                     PlanAnualPdfView)
from .views.plan_unidad_views import (PlanUnidadListView,
                                      PlanUnidadCreateView,
                                      PlanUnidadUpdateView,
                                      PlanUnidadDeleteView,
                                      PlanUnidadDuplicateView,
                                      PlanUnidadPdfView)
from .views.plan_destrezas_views import (PlanDestrezasListView,
                                         PlanDestrezasCreateView,
                                         PlanDestrezasUpdateView,
                                         PlanDestrezasDeleteView,
                                         PlanDestrezasDuplicateView,
                                         PlanDestrezasPdfView)
from .views.ajax_views import (LoadCursosView, LoadDestrezasView,
                               LoadObjetivosView, LoadUnidadesView)

urlpatterns = [
     path('', PlanificacionesTemplateView.as_view(),
          name="planificaciones"),
     path('plan_clase/list/', PlanClaseListView.as_view(),
          name="plan_clase_list"),
     path('plan_clase/create/', plan_clase_create,
          name="plan_clase_create"),
     path('plan_clase/update/<int:pk>/<slug:slug>/', plan_clase_update,
          name="plan_clase_update"),
     path('plan_clase/delete/<int:pk>/', PlanClaseDeleteView.as_view(),
          name="plan_clase_delete"),
     path('plan_clase/duplicate/<int:pk>/',
          PlanClaseDuplicateView.as_view(),
          name="plan_clase_duplicate"),
     path('plan_anual/list/', PlanAnualListView.as_view(),
          name="plan_anual_list"),
     path('plan_anual/create/', PlanAnualCreateView.as_view(),
          name="plan_anual_create"),
     path('plan_anual/update/<int:pk>/<slug:slug>/',
          PlanAnualUpdateView.as_view(),
          name="plan_anual_update"),
     path('plan_anual/delete/<int:pk>/', PlanAnualDeleteView.as_view(),
          name="plan_anual_delete"),
     path('plan_anual/duplicate/<int:pk>/',
          PlanAnualDuplicateView.as_view(),
          name="plan_anual_duplicate"),
     path('plan_unidad/list/', PlanUnidadListView.as_view(),
          name="plan_unidad_list"),
     path('plan_unidad/create/',
          PlanUnidadCreateView.as_view(),
          name="plan_unidad_create"),
     path('plan_unidad/update/<int:pk>/<slug:slug>/',
          PlanUnidadUpdateView.as_view(),
          name="plan_unidad_update"),
     path('plan_unidad/delete/<int:pk>/', PlanUnidadDeleteView.as_view(),
          name="plan_unidad_delete"),
     path('plan_unidad/duplicate/<int:pk>/',
          PlanUnidadDuplicateView.as_view(),
          name="plan_unidad_duplicate"),
     path('plan_destrezas/list/', PlanDestrezasListView.as_view(),
          name="plan_destrezas_list"),
     path('plan_destrezas/create/', PlanDestrezasCreateView.as_view(),
          name="plan_destrezas_create"),
     path('plan_destrezas/update/<int:pk>/<slug:slug>/',
          PlanDestrezasUpdateView.as_view(),
          name="plan_destrezas_update"),
     path('plan_destrezas/delete/<int:pk>/',
          PlanDestrezasDeleteView.as_view(),
          name="plan_destrezas_delete"),
     path('plan_destrezas/duplicate/<int:pk>/',
          PlanDestrezasDuplicateView.as_view(),
          name="plan_destrezas_duplicate"),

     # Ajax urls
     # templates: select, checklist
     path('ajax/cursos/<str:template>/', LoadCursosView.as_view(),
          name="ajax_load_cursos"),
     path('ajax/unidades/', LoadUnidadesView.as_view(),
          name="ajax_load_unidades"),
     # options: area, curso, unidad
     path('ajax/objetivos/<str:option>/', LoadObjetivosView.as_view(),
          name="ajax_load_objetivos"),
     # templates: select, checklist
     path('ajax/destrezas/<str:template>/',
          LoadDestrezasView.as_view(),
          name="ajax_load_destrezas"),
     path('plan_clase/pdf/<int:pk>/', PlanClasePdfView.as_view(),
          name='plan_clase_pdf'),
     path('plan_anual/pdf/<int:pk>/', PlanAnualPdfView.as_view(),
          name='plan_anual_pdf'),
     path('plan_unidad/pdf/<int:pk>/', PlanUnidadPdfView.as_view(),
          name='plan_unidad_pdf'),
     path('plan_destrezas/pdf/<int:pk>/', PlanDestrezasPdfView.as_view(),
          name='plan_destrezas_pdf'),
]
