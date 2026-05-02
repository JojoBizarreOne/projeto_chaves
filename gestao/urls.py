from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imovel/<int:id>', views.detalhe_imovel, name='detalhe'),
]