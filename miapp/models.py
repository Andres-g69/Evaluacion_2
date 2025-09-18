from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    # Hereda campos como username, email, password, etc.
    puntuacion_total = models.IntegerField(default=0)
    ranking_posicion = models.IntegerField(null=True, blank=True)


    # Sobrescribimos los campos groups y user_permissions para evitar colisiones
    groups = models.ManyToManyField(
        Group,
        nombre_usuario='usuarios',  # Cambia related_name para evitar conflicto
        blank=True,
        help_text='Los grupos a los que pertenece el usuario.',
        verbose_name='grupos',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        nombre_usuario='usuarios',  # Cambia related_name para evitar conflicto
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario',
    )

    def __str__(self):
        return self.username

class Reto(models.Model):
    DIFICULTADES = [
        ('F', 'Fácil'),
        ('M', 'Medio'),
        ('D', 'Difícil'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    respuesta_correcta = models.TextField()
    dificultad = models.CharField(max_length=1, choices=DIFICULTADES)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='retos')

    def __str__(self):
        return self.titulo


class Respuesta(models.Model):
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE, related_name='respuestas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='respuestas')
    respuesta_usuario = models.TextField()
    es_correcta = models.BooleanField(default=False)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    puntos_obtenidos = models.IntegerField(default=0)

    def __str__(self):
        return f"Respuesta de {self.usuario} al reto {self.reto}"



