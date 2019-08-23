from django import forms
from django.forms import ModelForm
from .models import Contato, Candidato


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'


class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'