
from django.contrib import admin
from django.urls import path
from .views import findex, fhistoria

urlpatterns = [
    path('', findex), #chama direto pelo servidor
    path('fhistoria/',fhistoria, name='fhistoria'),
    path('findex/',findex, name='findex'), #cria link de url



]
