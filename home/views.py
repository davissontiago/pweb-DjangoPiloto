from django.shortcuts import HttpResponse ,render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')
    
def ajuda(request):
    return render(request, 'ajuda.html')

def exibir_item(request, id):
    return render(request, 'exibir_item.html', {'id':id})

def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario':usuario})

def dia_semana(request, dia):
    dias_semana = {
        "1":"Domingo",
        "2":"Segunda-Feira",
        "3":"Terça-Feira",
        "4":"Quarta-Feira",
        "5":"Quinta-Feira",
        "6":"Sexta-Feira",
        "7":"Sábado"
    }
    
    dia_nome = dias_semana.get(str(dia))
    
    if dia_nome:
        return render(request, 'dia_semana.html', {'dia': dia_nome})
    else:
        return HttpResponse("Dia inválido! Digite um número de 1 a 7.")
