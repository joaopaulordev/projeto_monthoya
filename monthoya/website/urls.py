from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name="homepage"),
    path('imoveis/', imoveis, name="imoveis"),
    path('imoveis-views/', imoveis_views, name="imoveis_views"),
    path('contato/', contato, name="contato"),
    path('imovel/<int:id_imovel>/', ver_imovel, name="ver_imovel"),
]