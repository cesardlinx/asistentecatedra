from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlanificacionesTemplateView.as_view(),
         name="planificaciones"),
    path('plan_clase/list/', views.PlanClaseListView.as_view(),
         name="plan_clase_list"),
    path('plan_clase/create/', views.plan_clase_create,
         name="plan_clase_create"),
    path('plan_clase/update/<int:pk>/<slug:slug>/', views.plan_clase_update,
         name="plan_clase_update"),
    path('plan_clase/delete/<int:pk>/', views.PlanClaseDeleteView.as_view(),
         name="plan_clase_delete"),
    path('plan_clase/duplicate/<int:pk>/',
         views.PlanClaseDuplicateView.as_view(),
         name="plan_clase_duplicate"),
    path('plan_clase/ajax/cursos/', views.load_cursos,
         name="ajax_load_cursos"),
    path('plan_clase/ajax/objetivos/', views.load_objetivos,
         name="ajax_load_objetivos"),
    path('plan_clase/ajax/destrezas/', views.load_destrezas,
         name="ajax_load_destrezas"),
    path('plan_clase/ajax/indicadores/', views.load_indicadores,
         name="ajax_load_indicadores"),
]
