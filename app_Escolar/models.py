# app_Escolar/models.py

from django.db import models

# ======================
# MODELO ESTUDIANTE
# ======================
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    num_matricula = models.CharField(max_length=20, unique=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.num_matricula}"


# ======================
# MODELO PROFESOR
# ======================
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dni = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"


# ======================
# MODELO MATERIA
# ======================
class Materia(models.Model):
    nombre_materia = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel_academico = models.CharField(max_length=50)
    es_obligatoria = models.BooleanField(default=True)
    horas_semanales = models.IntegerField()

    def __str__(self):
        return self.nombre_materia


# ======================
# MODELO CURSO
# ======================
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')
    horario = models.CharField(max_length=100)
    aula = models.CharField(max_length=50)
    nivel_educativo = models.CharField(max_length=50)
    costo_curso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre_curso} - {self.profesor.nombre} {self.profesor.apellido}"


# ======================
# MODELO INSCRIPCION
# ======================
class Inscripcion(models.Model):
    ESTADO_CHOICES = [
        ('Activa', 'Activa'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
        ('Suspendida', 'Suspendida'),
    ]
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado_inscripcion = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Activa')
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.curso.nombre_curso}"


# ======================
# MODELO ASISTENCIA
# ======================
class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='asistencias')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='asistencias')
    fecha_clase = models.DateField()
    presente = models.BooleanField(default=True)
    justificacion = models.TextField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.curso.nombre_curso} - {self.fecha_clase}"


# ======================
# MODELO CALIFICACION
# ======================
class Calificacion(models.Model):
    TIPO_EVALUACION_CHOICES = [
        ('Examen', 'Examen'),
        ('Taller', 'Taller'),
        ('Proyecto', 'Proyecto'),
        ('Participación', 'Participación'),
        ('Tarea', 'Tarea'),
    ]
    
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, related_name='calificaciones')
    tipo_evaluacion = models.CharField(max_length=50, choices=TIPO_EVALUACION_CHOICES)
    fecha_evaluacion = models.DateField()
    puntaje = models.DecimalField(max_digits=5, decimal_places=2)
    ponderacion = models.DecimalField(max_digits=3, decimal_places=2, default=1.0)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.inscripcion.estudiante.nombre} - {self.tipo_evaluacion} - {self.puntaje}"