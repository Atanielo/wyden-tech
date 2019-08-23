from django.contrib import admin

from .models import(
    Contato,
    Candidato
)

#fields
#list_display
#list_filter
#search_fields


class ContatoAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email', 'telefone')
    list_display = ('nome', 'email', 'telefone')


class CandidatoAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email', 'cpf','data_nascimento','arquivo')
    list_display = ('nome', 'email', 'cpf','data_nascimento', 'arquivo')






admin.site.register(Contato, ContatoAdmin)
admin.site.register(Candidato, CandidatoAdmin)
