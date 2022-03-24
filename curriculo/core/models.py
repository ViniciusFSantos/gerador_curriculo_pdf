from uuid import UUID
import uuid

from django.db import models
    
class Candidato(models.Model):
    estado_civil_choices = (
        ('Solteiro(a)', 'Solteiro(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Divorsiado(a)', 'Divorsiado(a)'),
        ('Viúvo(a)', 'Viúvo(a)'),
    )
    
    key =  models.UUIDField(primary_key='True', default=uuid.uuid1, editable='False', verbose_name='PK')
    nome = models.CharField(max_length=100, verbose_name='nome_completo')
    idade = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='idade')
    estado_civil = models.CharField(max_length=14, choices=estado_civil_choices, blank=False, null=False, verbose_name='estado_civil')
    endereco = models.CharField(max_length=100, help_text='Bairro, Cidade - UF', verbose_name='endereco')
    email = models.EmailField(max_length=100, verbose_name='email')
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='telefone')
    linkedin = models.URLField(max_length=150, verbose_name='linkedin')
    objetivo = models.TextField(max_length=200)
    formacao_academica = models.TextField(max_length=200)
    idiomas = models.CharField(max_length=100, verbose_name='idioma')
    outras_qualificacoes = models.TextField(max_length=200, verbose_name='Qualificações')
    experiencia1 = models.TextField(max_length=200, verbose_name='exp1')
    experiencia2 = models.TextField(max_length=200, verbose_name='exp2')
    experiencia3 =  models.TextField(max_length=200, verbose_name='exp3')
    
    
