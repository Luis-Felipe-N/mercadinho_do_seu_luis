from django.urls import path
from .views import *

app_name = 'mercado'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('produto/<int:id>/', ProdutoView.as_view(), name="produto")
]
