from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('us_nombre','us_direccion','us_telefono')
    search_fields= ('us_nombre','us_telefono')
    list_filter=('us_nombre')
    ordering=('us_nombre')

admin.site.register(Usuario,UsuarioAdmin)
