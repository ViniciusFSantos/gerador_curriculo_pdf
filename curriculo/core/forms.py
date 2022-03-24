import uuid
from django import forms
from .models import Candidato

class NewCandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        context_object_name = 'candidato_form'
        random_key = forms.UUIDField()
        fields= ('nome', 'idade', 'estado_civil', 'endereco', 'email', 'telefone', 'linkedin', 'objetivo', 'formacao_academica', 'idiomas', 'outras_qualificacoes', 'experiencia1', 'experiencia2', 'experiencia3')
    