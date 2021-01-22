from django.shortcuts import render, redirect
from .models import (
    Pessoa, Veiculo, MovRotativo,
    Mensalista, MovMensalista
 )
from .forms import (
    PessoaForm, VeiculoForm, movRotativoForm,
    mensalistaForm, movMensalistaForm
)


def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, "core/index.html", context)
    # return render(request, "base.html")
    
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form':form}
    # a chave do dicionário pode ser qualquer nome, mas o valor == objeto criado
    return render(request, 'core/lista_pessoas.html', data)

def cadastra_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def atualiza_pessoa(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/atualiza_pessoa.html', data)

def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect("core_lista_pessoas")   
    else: 
        return render(request, 'core/delete_confirme.html', {'obj':pessoa})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos':veiculos, 'form':form }
    return render(request, 'core/lista_veiculos.html', data)

def cadastra_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def atualiza_veiculo(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/atualiza_veiculo.html', data)


def delete_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect("core_lista_veiculos")   
    else: 
        return render(request, 'core/delete_confirme.html', {'obj':veiculo})



def lista_rotativo(request):
    rotativos = MovRotativo.objects.all()
    form = movRotativoForm()
    data = {'rotativos':rotativos, 'form':form }    
    return render(request, 'core/lista_rotativo.html', data)

def cadastra_movRotativo(request):
    form = movRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_rotativo')

def atualiza_movRotativo(request, id):
    data = {}
    movRotativo = MovRotativo.objects.get(id=id)
    form = movRotativoForm(request.POST or None, instance=movRotativo)
    data['movRotativo'] = movRotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_rotativo')
    else:
        return render(request, 'core/atualiza_movRotativo.html', data)

def delete_movRotativo(request, id):
    movRotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movRotativo.delete()
        return redirect('core_lista_rotativo')   
    else: 
        return render(request, 'core/delete_confirme.html', {'obj':movRotativo})



def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = mensalistaForm()
    data = {'mensalistas':mensalistas, 'form':form}
    return render(request, 'core/lista_mensalista.html', data)

def cadastra_mensalista(request):
    form = mensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')

def atualiza_mensalista(request, id):
    data = {}
    mensalista= Mensalista.objects.get(id=id)
    form = mensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/atualiza_mensalista.html', data)

def delete_mensalista(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')   
    else: 
        return render(request, 'core/delete_confirme.html', {'obj':mensalista})




def lista_mov_mensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = movMensalistaForm()
    data = {'mov_mensalistas':mov_mensalistas, 'form':form}
    return render(request, 'core/mov_mensalista.html', data)

def cadastra_movMensalista(request):
    form = movMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_mensalista') 

def atualiza_movMensalista(request, id):
    data = {}
    movMensalista= MovMensalista.objects.get(id=id)
    form = movMensalistaForm(request.POST or None, instance=movMensalista)
    data['movMensalista'] = movMensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mensalista')
    else:
        return render(request, 'core/atualiza_movMensalista.html', data)

def delete_movMensalista(request, id):
    movMensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movMensalista.delete()
        return redirect('core_lista_mov_mensalista')   
    else: 
        return render(request, 'core/delete_confirme.html', {'obj':movMensalista})

   