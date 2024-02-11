from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    pagina = models.IntegerField()
    obs = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return f"{self.titulo} {self.pagina} {self.usuario}"