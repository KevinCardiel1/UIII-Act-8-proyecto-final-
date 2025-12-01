# app_Escolar/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ruta inicio
    path('', views.inicio_escolar, name='inicio_escolar'),

    # Rutas para Estudiantes
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/', views.ver_estudiantes, name='ver_estudiantes'),
    path('estudiantes/actualizar/<int:pk>/', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('estudiantes/borrar/<int:pk>/', views.borrar_estudiante, name='borrar_estudiante'),

    # Rutas para Profesores
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/', views.ver_profesores, name='ver_profesores'),
    path('profesores/actualizar/<int:pk>/', views.actualizar_profesor, name='actualizar_profesor'),
    path('profesores/borrar/<int:pk>/', views.borrar_profesor, name='borrar_profesor'),

    # Rutas para Materias
    path('materias/agregar/', views.agregar_materia, name='agregar_materia'),
    path('materias/', views.ver_materias, name='ver_materias'),
    path('materias/actualizar/<int:pk>/', views.actualizar_materia, name='actualizar_materia'),
    path('materias/borrar/<int:pk>/', views.borrar_materia, name='borrar_materia'),

    # Rutas para Cursos
    path('cursos/agregar/', views.agregar_curso, name='agregar_curso'),
    path('cursos/', views.ver_cursos, name='ver_cursos'),
    path('cursos/actualizar/<int:pk>/', views.actualizar_curso, name='actualizar_curso'),
    path('cursos/borrar/<int:pk>/', views.borrar_curso, name='borrar_curso'),

    # Rutas para Inscripciones
    path('inscripciones/agregar/', views.agregar_inscripcion, name='agregar_inscripcion'),
    path('inscripciones/', views.ver_inscripciones, name='ver_inscripciones'),
    path('inscripciones/actualizar/<int:pk>/', views.actualizar_inscripcion, name='actualizar_inscripcion'),
    path('inscripciones/borrar/<int:pk>/', views.borrar_inscripcion, name='borrar_inscripcion'),

    # Rutas para Asistencias
    path('asistencias/agregar/', views.agregar_asistencia, name='agregar_asistencia'),
    path('asistencias/', views.ver_asistencias, name='ver_asistencias'),
    path('asistencias/actualizar/<int:pk>/', views.actualizar_asistencia, name='actualizar_asistencia'),
    path('asistencias/borrar/<int:pk>/', views.borrar_asistencia, name='borrar_asistencia'),

    # Rutas para Calificaciones
    path('calificaciones/agregar/', views.agregar_calificacion, name='agregar_calificacion'),
    path('calificaciones/', views.ver_calificaciones, name='ver_calificaciones'),
    path('calificaciones/actualizar/<int:pk>/', views.actualizar_calificacion, name='actualizar_calificacion'),
    path('calificaciones/borrar/<int:pk>/', views.borrar_calificacion, name='borrar_calificacion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)