from django.urls import path
from .views import *

app_name = 'mercado'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('produto/<int:id>/', ProdutoView.as_view(), name="produto"),
    path('produto/category/<slug:slug>/', CategoriaProdutoView.as_view(), name="categoria-produto"),
    # path('produto/add/', AdicionarProdutoView.as_view(), name="adicionar-produto"),
    # path('produto/edit/<int:id>', EditProdutoView.as_view(), name="editar-produto"),
    # path('produto/delete/<int:id>', DeleteProdutoView.as_view(), name="delete-produto")
]
