from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Fragmento
from .forms import FormularioFragmento



# Create your views here.
def homeView(request):
    return HttpResponse("home page")

def sucesso(request, pk):
    frag = get_object_or_404(Fragmento, pk=pk )
    ava = frag.avaliaEstagio()
    return HttpResponse(f"Estágio de regeneração: {ava}")


def pagFormulario(request):
    form = FormularioFragmento
    if request.method == "POST":
        form = FormularioFragmento(request.POST)
        fragmento = form.save()
        return redirect('sucesso', pk=fragmento.pk)
    
    return render(request,"html/formulario.html",{"form": form})





