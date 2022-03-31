from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('produto/<int:id>/', ProdutoView, name="produto")
]
