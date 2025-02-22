from django.shortcuts import render, redirect
from .models import *

# Create your views he
def homepage(request):
    imoveis = Imovel.objects.filter(ativo=True).order_by('titulo')
    imoveis_destaque = imoveis.filter(destaque=True).order_by("titulo")
    bairros = Bairro.objects.filter(isHomepage=True).order_by("descricao")  
            
    context = {"imoveis": imoveis, "imoveis_destaque": imoveis_destaque, "bairros": bairros}
    return render(request, 'homepage.html', context)


def imoveis(request):
    imoveis = Imovel.objects.filter(ativo=True).order_by('titulo')
    context = {"imoveis": imoveis}
    return render(request, 'imoveis.html', context)


def imoveis_views(request):
    imoveis = Imovel.objects.filter(ativo=True).order_by('titulo')
    imoveis_views = imoveis.order_by("-views")       
    context = {"imoveis_views": imoveis_views}
    return render(request, 'imoveis-views.html', context)


def ver_imovel(request, id_imovel):
    imovel = Imovel.objects.get(id=id_imovel)
    if request.method == "POST":
        dados = request.POST.dict()
        imovelContato = ImovelContato.objects.create(imovel=imovel,
                                         nome=dados.get("nome"), 
                                         email=dados.get("email"), 
                                         assunto=dados.get("assunto"),
                                         telefone=dados.get("telefone"),
                                         mensagem=dados.get("mensagem"))
        imovelContato.save()
        return redirect("homepage")        
    else:        
        imovel_fotos = ImovelFoto.objects.filter(imovel=imovel)
        context = {"imovel": imovel, "imovel_fotos": imovel_fotos}
        return render(request, 'ver_imovel.html', context)
    

def contato(request):
    if request.method == "POST":
        dados = request.POST.dict()
        contato = Contato.objects.create(nome=dados.get("nome"), 
                                         email=dados.get("email"), 
                                         assunto=dados.get("assunto"),
                                         telefone=dados.get("telefone"),
                                         mensagem=dados.get("mensagem"))
        contato.save()
        return redirect("homepage")        
    else:
        context = {}
        return render(request, "contato.html", context)
