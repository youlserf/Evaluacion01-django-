from django.urls import path
from . import views
app_name = 'encuesta_region'
urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('<int:region_id>/', views.detalle, name='detalle'),

    # ex: /encuesta/5/resultados/
    path('<int:region_id>/resultados/', views.resultados, name='resultados'),
    # ex: /encuesta/5/voto/
    path('<int:region_id>/voto/', views.votar, name='votar'),

    path('<int:region_id>/eliminar/', views.eliminar, name='eliminar'),

    path('<int:region_id>/actualizar_view/', views.actualizar_view, name='actualizar_view'),

    path('actualizar/', views.actualizar, name='actualizar'),
]