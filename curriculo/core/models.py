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
    nome = models.CharField(max_length=100, verbose_name='Nome Completo')
    idade = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='Idade')
    estado_civil = models.CharField(max_length=14, choices=estado_civil_choices, blank=False, null=False, verbose_name='Estado Civil')
    endereco = models.CharField(max_length=100, help_text='Ex:  Bairro, Cidade - UF', verbose_name='Endereço')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone')
    linkedin = models.URLField(max_length=150, verbose_name='LinkedIn')
    objetivo = models.TextField(max_length=300)
    formacao_academica = models.TextField(max_length=400, verbose_name='Formação Acadêmica')
    idiomas = models.CharField(max_length=100, verbose_name='Idioma')
    outras_qualificacoes = models.TextField(max_length=800, verbose_name='Qualificações')
    experiencia1 = models.TextField(max_length=800, verbose_name='Experiência Profissional 1')
    experiencia2 = models.TextField(max_length=800, verbose_name='Experiência Profissional 2')
    experiencia3 =  models.TextField(max_length=800, verbose_name='Experiência Profissional 3')
    
    
