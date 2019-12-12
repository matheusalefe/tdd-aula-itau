from django.shortcuts import render, redirect
from .models import Aluno, Usuario

# Create your views here.

def index(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.nome = request.POST['nome']
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        
    return render(request, 'index.html')

def listar(request):
    listar_aluno = Aluno.objects.filter(ativo=True).all()
    args = {
        'listar_alunos': listar_aluno
    }
    return render(request, 'lista.html', args)

def deletar(request, id):
    item = Aluno.objects.get(id=id)
    if item is not None:
        item.ativo = False
        item.save()
        return redirect('alunos/lista')
    return render(request, 'lista.html')