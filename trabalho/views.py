from django.shortcuts import render
from trabalho.models import Aluno


# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    testChave = {
        'alunos': alunos
    }
    return render(request, 'index.html', testChave)


def aluno(request, id):
    alunos = Aluno.objects.get(id=id)
    testChave = {
        'alunos': alunos
    }
    return render(request, 'aluno.html', testChave)
