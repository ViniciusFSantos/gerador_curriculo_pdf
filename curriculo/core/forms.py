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
        self.fields['endereco'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex: Centro, Volta Redonda - RJ'})
        self.fields['email'].widget.attrs.update({'class':'special-placeholders', 'placeholder':'Ex: email@provedor.com'})
        self.fields['telefone'].widget.attrs.update({'class':'special-placeholders', 'placeholder':'Ex: (24) 9983-6570'})
        self.fields['linkedin'].widget.attrs.update({'class':'special-placeholders', 'placeholder':'Ex:  https://linkedin.com/ronaldocerqueira'})
        self.fields['formacao_academica'].widget.attrs.update({'class':'special-placeholders', 'placeholder':'Ex: ', 'rows':'4'})
        self.fields['idiomas'].widget.attrs.update({'class':'special-placeholders','placeholder':'Inglês Básico - Espanhol Fluente'})
        self.fields['outras_qualificacoes'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex:', 'rows':'4'})
        self.fields['empresa1'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex: Contabilidade União - 03/2018 a 02/2022'})
        self.fields['experiencia1'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex: ', 'rows':'4'})
        self.fields['empresa2'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex: Laboratórios Lux - 01/2011 a 08/2016'})
        self.fields['experiencia2'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex: ', 'rows':'4'})
        self.fields['empresa3'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex: Mecânica Teixeira - 05/2009 a 06/2010'})
        self.fields['experiencia3'].widget.attrs.update({'class':'special-placeholders','placeholder':'Ex: ', 'rows':'4'})

