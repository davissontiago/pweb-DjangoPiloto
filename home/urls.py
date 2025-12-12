from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('produto/', views.produto, name='produto'),
    path('produto/form', views.salvar_produto , name='salvar_produto'),
    path('produto/detalhes/<int:id>', views.detalhes_produto , name='detalhes_produto'),
    path('produto/editar/<int:id>', views.editar_produto , name='editar_produto'),
    path('produto/excluir/<int:id>', views.excluir_produto , name='excluir_produto'),
    path('item/<int:id>', views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>', views.perfil , name='perfil'),
    path('diasemana/<int:dia>', views.dia_semana, name='dia_semana'),
    path('home/', views.home, name='home')
]