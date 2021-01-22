
from django.urls import path, include
from .views import (
    home, 
    lista_pessoas,
    lista_veiculos,
    lista_rotativo,
    lista_mensalistas,
    lista_mov_mensalista,
    cadastra_pessoa, 
    cadastra_veiculo,
    cadastra_movRotativo,
    cadastra_mensalista,
    cadastra_movMensalista,
    atualiza_pessoa, 
    atualiza_veiculo,
    atualiza_movRotativo,
    atualiza_mensalista,
    atualiza_movMensalista, 
    delete_pessoa,
    delete_veiculo,
    delete_movRotativo, 
    delete_mensalista,
    delete_movMensalista

)

urlpatterns = [
    path('core/', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('cadastra_pessoa/', cadastra_pessoa, name='core_cadastra_pessoa'),
    path('atualiza_pessoa/<int:id>/', atualiza_pessoa, name='core_atualiza_pessoa'),
    path('delete_pessoa/<int:id>/', delete_pessoa, name='core_delete_pessoa'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('cadastra_veiculo/', cadastra_veiculo, name='core_cadastra_veiculo'),
    path('atualiza_veiculo/<int:id>/', atualiza_veiculo, name='core_atualiza_veiculo'),
    path('delete_veiculo/<int:id>', delete_veiculo, name='core_delete_veiculo'),

    path('MovRotativo/', lista_rotativo, name='core_lista_rotativo'),
    path('cadastra_movRotativo/', cadastra_movRotativo, name='core_cadastra_movRotativo'),
    path('atualiza_movRotativo/<int:id>/', atualiza_movRotativo, name='core_atualiza_movRotativo'),
    path('delete_movRotativo/<int:id>/', delete_movRotativo, name='core_delete_movRotativo'),

    path('mensalista/', lista_mensalistas, name='core_lista_mensalista'),
    path('cadastra_mensalista/', cadastra_mensalista, name='core_cadastra_mensalista'),
    path('atualiza_mensalista/<int:id>/', atualiza_mensalista, name='core_atualiza_mensalista'),
    path('delete_mensalista/<int:id>/', delete_mensalista, name='core_delete_mensalista'),


    path('mov_mensalista/', lista_mov_mensalista, name='core_lista_mov_mensalista'),
    path('cadastra_movMensalista/', cadastra_movMensalista, name='core_cadastra_movMensalista'),       
    path('atualiza_movMensalista/<int:id>/', atualiza_movMensalista, name='core_atualiza_movMensalista'),
    path('delete_movMensalista/<int:id>/', delete_movMensalista, name='core_delete_movMensalista'),      
]
