# app_Escolar/admin.py

from django.contrib import admin
from .models import Estudiante, Profesor, Materia, Curso, Inscripcion, Asistencia, Calificacion


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('num_matricula', 'nombre', 'apellido', 'email', 'telefono', 'fecha_inscripcion')
    list_filter = ('fecha_inscripcion', 'genero')
    search_fields = ('nombre', 'apellido', 'num_matricula', 'email')
    ordering = ('apellido', 'nombre')


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'email', 'especialidad', 'salario')
    list_filter = ('especialidad', 'fecha_contratacion')
    search_fields = ('nombre', 'apellido', 'dni', 'email')
    ordering = ('apellido', 'nombre')


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_materia', 'nivel_academico', 'es_obligatoria', 'horas_semanales')
    list_filter = ('nivel_academico', 'es_obligatoria')
    search_fields = ('nombre_materia',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre_curso', 'profesor', 'nivel_educativo', 'aula', 'creditos', 'costo_curso')
    list_filter = ('nivel_educativo', 'profesor')
    search_fields = ('nombre_curso', 'profesor__nombre', 'profesor__apellido')
    raw_id_fields = ('profesor',)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'curso', 'fecha_inscripcion', 'estado_inscripcion', 'nota_final')
    list_filter = ('estado_inscripcion', 'fecha_inscripcion')
    search_fields = ('estudiante__nombre', 'estudiante__apellido', 'curso__nombre_curso')
    raw_id_fields = ('estudiante', 'curso')


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_clase', 'presente')
    list_filter = ('presente', 'fecha_clase')
    search_fields = ('estudiante__nombre', 'estudiante__apellido', 'curso__nombre_curso')
    raw_id_fields = ('estudiante', 'curso')


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('inscripcion', 'tipo_evaluacion', 'fecha_evaluacion', 'puntaje', 'ponderacion')
    list_filter = ('tipo_evaluacion', 'fecha_evaluacion')
    search_fields = ('inscripcion__estudiante__nombre', 'inscripcion__estudiante__apellido')
    raw_id_fields = ('inscripcion',)