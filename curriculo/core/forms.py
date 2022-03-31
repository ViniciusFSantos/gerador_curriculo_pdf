import uuid
from django import forms
from .models import Candidato

class NewCandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        context_object_name = 'candidato_form'
        fields = ('nome', 'idade', 'estado_civil', 'endereco', 'email', 'telefone', 'linkedin', 'objetivo', 'formacao_academica', 'idiomas', 'outras_qualificacoes', 'empresa1', 'experiencia1', 'empresa2', 'experiencia2', 'empresa3', 'experiencia3')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idiomas'].widget.attrs.update({'placeholder':'Teste'})
        self.fields['email'].widget.attrs.update({'placeholder':'email@provedor.com'})
