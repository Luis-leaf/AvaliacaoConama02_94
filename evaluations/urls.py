from django.urls import path
from . import views

urlpatterns = [
    path('',views.pagFormulario, name="formulario" ),
    path('sucesso/<int:pk>',views.sucesso, name='sucesso')
]