from django.shortcuts import render, redirect
from .models import Contato, Candidato
from django.contrib import messages


def home(request):
    return render(request, 'core/index.html')


def contato_novo(request):
    if request.method == 'POST':

            contato = {}
            contato['nome'] = request.POST.get('nome')
            contato['telefone'] = request.POST.get('telefone')
            contato['email'] = request.POST.get('email')
            contato['mensagem'] = request.POST.get('mensagem')

            Contato.objects.create(**contato)
    return redirect('core_home')



def candidato_novo(request):
    if request.method == 'POST':
        try:
            candidato = {}
            candidato['nome'] = request.POST.get('nome')
            candidato['email'] = request.POST.get('email')
            candidato['nacionalidade'] = request.POST.get('nacionalidade')
            candidato['cpf'] = request.POST.get('cpf')
            candidato['telefone'] = request.POST.get('telefone')
            candidato['data_nascimento'] = request.POST.get('data_nascimento')
            candidato['genero'] = request.POST.get('genero')
            candidato['estado_civil'] = request.POST.get('estado_civil')
            candidato['deficiencia'] = request.POST.get('deficiencia')
            candidato['tipo_deficiencia'] = request.POST.get('tipo_deficiencia')
            candidato['cep'] = request.POST.get('cep')
            candidato['logradouro'] = request.POST.get('logradouro')
            candidato['numero'] = request.POST.get('numero')
            candidato['complemento'] = request.POST.get('complemento')
            candidato['bairro'] = request.POST.get('bairro')
            candidato['estado'] = request.POST.get('estado')
            candidato['cidade'] = request.POST.get('cidade')
            candidato['matricula'] = request.POST.get('matricula')
            candidato['curso'] = request.POST.get('curso')
            candidato['periodo'] = request.POST.get('periodo')
#            if request.method == 'POST':
#                candidato['arquivo'] = request.FILES.get('arquivo')

            Candidato.objects.create(**candidato)
        except Exception as e:
                messagem = str(e)
        else:
            mensagem = 'Contato realizado com sucesso'

    return redirect('core_home')


'''def candidato_novo(request):
    if request.method == 'POST':
        formu = CandidatoForm(request.POST, request.FILES)
    if formu.is_valid():
        formu.save()
    return redirect('core_home')'''


def login(request):
    return redirect('admin/')

