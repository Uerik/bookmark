from django.contrib import admin
from .models import Livros
# Register your models here.

class LivrosADM(admin.ModelAdmin):
    list_display = ('titulo' , 'pagina', 'usuario')

admin.site.register(Livros, LivrosADM)