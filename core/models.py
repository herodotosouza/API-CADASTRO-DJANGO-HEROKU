from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField('Categoria', max_length=100)

    def __str__(self):
        return self.nome_categoria