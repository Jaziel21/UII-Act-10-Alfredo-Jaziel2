from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_autores, name='listar_autores'),
    path('agregar/', views.agregar_autor, name='agregar_autor'),
    path('<int:autor_id>/', views.ver_autor, name='ver_autor'),
    path('editar/<int:autor_id>/', views.editar_autor, name='editar_autor'),
    path('eliminar/<int:autor_id>/', views.eliminar_autor, name='eliminar_autor'),
]