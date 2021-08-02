from django.db import models


# Create your models here.
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=150)
    ingresso = models.CharField('Período de Ingresso', max_length=7)
    nota = models.IntegerField('Nota - Web Avançado')
    situacao = models.CharField('Situação', max_length=10)

    def __str__(self):
        return self.nome