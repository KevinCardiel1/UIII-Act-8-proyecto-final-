# app_Escolar/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Profesor, Materia, Curso, Inscripcion, Asistencia, Calificacion
from datetime import date

# =================== VISTAS INICIO ===================
def inicio_escolar(request):
    """Vista principal del sistema de gestión escolar"""
    estudiantes_count = Estudiante.objects.count()
    profesores_count = Profesor.objects.count()
    cursos_count = Curso.objects.count()
    inscripciones_count = Inscripcion.objects.count()
    # Contadores adicionales solicitados
    materias_count = Materia.objects.count()
    asistencias_count = Asistencia.objects.count()
    calificaciones_count = Calificacion.objects.count()
    
    context = {
        'estudiantes_count': estudiantes_count,
        'profesores_count': profesores_count,
        'cursos_count': cursos_count,
        'inscripciones_count': inscripciones_count,
        'materias_count': materias_count,
        'asistencias_count': asistencias_count,
        'calificaciones_count': calificaciones_count,
    }
    return render(request, 'app_Escolar/inicio.html', context)


# =================== VISTAS ESTUDIANTE ===================
def agregar_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        genero = request.POST['genero']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        num_matricula = request.POST['num_matricula']

        Estudiante.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            direccion=direccion,
            telefono=telefono,
            email=email,
            num_matricula=num_matricula
        )
        return redirect('ver_estudiantes')
    return render(request, 'app_Escolar/estudiantes/agregar_estudiante.html')


def ver_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'app_Escolar/estudiantes/ver_estudiantes.html', {'estudiantes': estudiantes})


def actualizar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.nombre = request.POST['nombre']
        estudiante.apellido = request.POST['apellido']
        estudiante.fecha_nacimiento = request.POST['fecha_nacimiento']
        estudiante.genero = request.POST['genero']
        estudiante.direccion = request.POST['direccion']
        estudiante.telefono = request.POST['telefono']
        estudiante.email = request.POST['email']
        estudiante.num_matricula = request.POST['num_matricula']
        estudiante.save()
        return redirect('ver_estudiantes')
    return render(request, 'app_Escolar/estudiantes/actualizar_estudiante.html', {'estudiante': estudiante})


def borrar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('ver_estudiantes')
    return render(request, 'app_Escolar/estudiantes/borrar_estudiante.html', {'estudiante': estudiante})


# =================== VISTAS PROFESOR ===================
def agregar_profesor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        telefono = request.POST['telefono']
        especialidad = request.POST['especialidad']
        fecha_contratacion = request.POST['fecha_contratacion']
        salario = request.POST['salario']
        dni = request.POST['dni']

        Profesor.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            especialidad=especialidad,
            fecha_contratacion=fecha_contratacion,
            salario=salario,
            dni=dni
        )
        return redirect('ver_profesores')
    return render(request, 'app_Escolar/profesores/agregar_profesor.html')


def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'app_Escolar/profesores/ver_profesores.html', {'profesores': profesores})


def actualizar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.nombre = request.POST['nombre']
        profesor.apellido = request.POST['apellido']
        profesor.email = request.POST['email']
        profesor.telefono = request.POST['telefono']
        profesor.especialidad = request.POST['especialidad']
        profesor.fecha_contratacion = request.POST['fecha_contratacion']
        profesor.salario = request.POST['salario']
        profesor.dni = request.POST['dni']
        profesor.save()
        return redirect('ver_profesores')
    return render(request, 'app_Escolar/profesores/actualizar_profesor.html', {'profesor': profesor})


def borrar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('ver_profesores')
    return render(request, 'app_Escolar/profesores/borrar_profesor.html', {'profesor': profesor})


# =================== VISTAS MATERIA ===================
def agregar_materia(request):
    if request.method == 'POST':
        nombre_materia = request.POST['nombre_materia']
        descripcion = request.POST['descripcion']
        nivel_academico = request.POST['nivel_academico']
        es_obligatoria = request.POST.get('es_obligatoria') == 'on'
        horas_semanales = request.POST['horas_semanales']

        Materia.objects.create(
            nombre_materia=nombre_materia,
            descripcion=descripcion,
            nivel_academico=nivel_academico,
            es_obligatoria=es_obligatoria,
            horas_semanales=horas_semanales
        )
        return redirect('ver_materias')
    return render(request, 'app_Escolar/materias/agregar_materia.html')


def ver_materias(request):
    materias = Materia.objects.all()
    return render(request, 'app_Escolar/materias/ver_materias.html', {'materias': materias})


def actualizar_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.nombre_materia = request.POST['nombre_materia']
        materia.descripcion = request.POST['descripcion']
        materia.nivel_academico = request.POST['nivel_academico']
        materia.es_obligatoria = request.POST.get('es_obligatoria') == 'on'
        materia.horas_semanales = request.POST['horas_semanales']
        materia.save()
        return redirect('ver_materias')
    return render(request, 'app_Escolar/materias/actualizar_materia.html', {'materia': materia})


def borrar_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('ver_materias')
    return render(request, 'app_Escolar/materias/borrar_materia.html', {'materia': materia})


# =================== VISTAS CURSO ===================
def agregar_curso(request):
    profesores = Profesor.objects.all()
    if request.method == 'POST':
        nombre_curso = request.POST['nombre_curso']
        descripcion = request.POST['descripcion']
        creditos = request.POST['creditos']
        profesor_id = request.POST['profesor']
        horario = request.POST['horario']
        aula = request.POST['aula']
        nivel_educativo = request.POST['nivel_educativo']
        costo_curso = request.POST['costo_curso']

        profesor = get_object_or_404(Profesor, pk=profesor_id)
        Curso.objects.create(
            nombre_curso=nombre_curso,
            descripcion=descripcion,
            creditos=creditos,
            profesor=profesor,
            horario=horario,
            aula=aula,
            nivel_educativo=nivel_educativo,
            costo_curso=costo_curso
        )
        return redirect('ver_cursos')
    return render(request, 'app_Escolar/cursos/agregar_curso.html', {'profesores': profesores})


def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'app_Escolar/cursos/ver_cursos.html', {'cursos': cursos})


def actualizar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    profesores = Profesor.objects.all()
    if request.method == 'POST':
        curso.nombre_curso = request.POST['nombre_curso']
        curso.descripcion = request.POST['descripcion']
        curso.creditos = request.POST['creditos']
        curso.profesor = get_object_or_404(Profesor, pk=request.POST['profesor'])
        curso.horario = request.POST['horario']
        curso.aula = request.POST['aula']
        curso.nivel_educativo = request.POST['nivel_educativo']
        curso.costo_curso = request.POST['costo_curso']
        curso.save()
        return redirect('ver_cursos')
    return render(request, 'app_Escolar/cursos/actualizar_curso.html', {'curso': curso, 'profesores': profesores})


def borrar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('ver_cursos')
    return render(request, 'app_Escolar/cursos/borrar_curso.html', {'curso': curso})


# =================== VISTAS INSCRIPCION ===================
def agregar_inscripcion(request):
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        estudiante_id = request.POST['estudiante']
        curso_id = request.POST['curso']
        estado = request.POST.get('estado_inscripcion', 'Activa')

        estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
        curso = get_object_or_404(Curso, pk=curso_id)
        
        Inscripcion.objects.create(
            estudiante=estudiante,
            curso=curso,
            estado_inscripcion=estado
        )
        return redirect('ver_inscripciones')
    return render(request, 'app_Escolar/inscripciones/agregar_inscripcion.html', {
        'estudiantes': estudiantes,
        'cursos': cursos
    })


def ver_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'app_Escolar/inscripciones/ver_inscripciones.html', {'inscripciones': inscripciones})


def actualizar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        inscripcion.estudiante = get_object_or_404(Estudiante, pk=request.POST['estudiante'])
        inscripcion.curso = get_object_or_404(Curso, pk=request.POST['curso'])
        inscripcion.estado_inscripcion = request.POST.get('estado_inscripcion', 'Activa')
        if request.POST.get('nota_final'):
            inscripcion.nota_final = request.POST['nota_final']
        inscripcion.save()
        return redirect('ver_inscripciones')
    return render(request, 'app_Escolar/inscripciones/actualizar_inscripcion.html', {
        'inscripcion': inscripcion,
        'estudiantes': estudiantes,
        'cursos': cursos
    })


def borrar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('ver_inscripciones')
    return render(request, 'app_Escolar/inscripciones/borrar_inscripcion.html', {'inscripcion': inscripcion})


# =================== VISTAS ASISTENCIA ===================
def agregar_asistencia(request):
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        estudiante_id = request.POST['estudiante']
        curso_id = request.POST['curso']
        fecha_clase = request.POST['fecha_clase']
        presente = request.POST.get('presente') == 'on'
        justificacion = request.POST.get('justificacion', '')
        comentarios = request.POST.get('comentarios', '')

        estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
        curso = get_object_or_404(Curso, pk=curso_id)
        
        Asistencia.objects.create(
            estudiante=estudiante,
            curso=curso,
            fecha_clase=fecha_clase,
            presente=presente,
            justificacion=justificacion,
            comentarios=comentarios
        )
        return redirect('ver_asistencias')
    return render(request, 'app_Escolar/asistencias/agregar_asistencia.html', {
        'estudiantes': estudiantes,
        'cursos': cursos
    })


def ver_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'app_Escolar/asistencias/ver_asistencias.html', {'asistencias': asistencias})


def actualizar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        asistencia.estudiante = get_object_or_404(Estudiante, pk=request.POST['estudiante'])
        asistencia.curso = get_object_or_404(Curso, pk=request.POST['curso'])
        asistencia.fecha_clase = request.POST['fecha_clase']
        asistencia.presente = request.POST.get('presente') == 'on'
        asistencia.justificacion = request.POST.get('justificacion', '')
        asistencia.comentarios = request.POST.get('comentarios', '')
        asistencia.save()
        return redirect('ver_asistencias')
    return render(request, 'app_Escolar/asistencias/actualizar_asistencia.html', {
        'asistencia': asistencia,
        'estudiantes': estudiantes,
        'cursos': cursos
    })


def borrar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        asistencia.delete()
        return redirect('ver_asistencias')
    return render(request, 'app_Escolar/asistencias/borrar_asistencia.html', {'asistencia': asistencia})


# =================== VISTAS CALIFICACION ===================
def agregar_calificacion(request):
    inscripciones = Inscripcion.objects.all()
    if request.method == 'POST':
        inscripcion_id = request.POST['inscripcion']
        tipo_evaluacion = request.POST['tipo_evaluacion']
        fecha_evaluacion = request.POST['fecha_evaluacion']
        puntaje = request.POST['puntaje']
        ponderacion = request.POST.get('ponderacion', '1.0')
        comentarios = request.POST.get('comentarios', '')

        inscripcion = get_object_or_404(Inscripcion, pk=inscripcion_id)
        
        Calificacion.objects.create(
            inscripcion=inscripcion,
            tipo_evaluacion=tipo_evaluacion,
            fecha_evaluacion=fecha_evaluacion,
            puntaje=puntaje,
            ponderacion=ponderacion,
            comentarios=comentarios
        )
        return redirect('ver_calificaciones')
    return render(request, 'app_Escolar/calificaciones/agregar_calificacion.html', {
        'inscripciones': inscripciones
    })


def ver_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'app_Escolar/calificaciones/ver_calificaciones.html', {'calificaciones': calificaciones})


def actualizar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    inscripciones = Inscripcion.objects.all()
    if request.method == 'POST':
        calificacion.inscripcion = get_object_or_404(Inscripcion, pk=request.POST['inscripcion'])
        calificacion.tipo_evaluacion = request.POST['tipo_evaluacion']
        calificacion.fecha_evaluacion = request.POST['fecha_evaluacion']
        calificacion.puntaje = request.POST['puntaje']
        calificacion.ponderacion = request.POST.get('ponderacion', '1.0')
        calificacion.comentarios = request.POST.get('comentarios', '')
        calificacion.save()
        return redirect('ver_calificaciones')
    return render(request, 'app_Escolar/calificaciones/actualizar_calificacion.html', {
        'calificacion': calificacion,
        'inscripciones': inscripciones
    })


def borrar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('ver_calificaciones')
    return render(request, 'app_Escolar/calificaciones/borrar_calificacion.html', {'calificacion': calificacion})
