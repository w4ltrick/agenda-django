from django.urls import path
from .views import home, lista_contatos, detalhes_contato

urlpatterns = [
    path('', home, name='home'),
    path('contatos/', lista_contatos, name='lista_contatos'),
    path('contatos/<int:id>/', detalhes_contato, name='detalhes_contato'),
]
