from unicodedata import name
from django import urls
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index' ),
    path('inserir_dados/', views.CandidatoFormView.as_view(), name='inserir_dados' ),
    path('inserir_dados/exp/pdf', views.render_pdf_view, name='exportar_dados_pdf'),
    path('inserir_dados/exp/pdf/error', views.ErrorView.as_view(), name='error_pdf')
]