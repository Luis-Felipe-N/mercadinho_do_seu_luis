from django.urls import path
from .views import *

app_name = 'mercado'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/category/<slug:slug>/', CategoriaProdutoView.as_view(), name="categoria-produto"),
    path('produto/all/', MeusProdutoView.as_view(), name="meus-produtos"),
    path('product/add/', AdicionarProdutoView.as_view(), name="adicionar-produto"),
    path('product/<int:pk>/edit', EditarProdutoView.as_view(), name="editar-produto"),
    # path('produto/delete/<int:id>', DeleteProdutoView.as_view(), name="delete-produto")
    path('product/<int:id>/', ProdutoView.as_view(), name="produto"),

    path('carrinho/', CarrinhoView.as_view(), name="carrinho")
]
