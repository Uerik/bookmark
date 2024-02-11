from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Livros
from django.contrib.auth.models import User

# Create your views here.
def add_new_item(request):
    template = loader.get_template('add.html')
    
    if request.method == 'POST':
        livroTitulo = request.POST['livroTitulo']
        livroPage = request.POST['livroPage']
        livroObs = request.POST['livroObs']
        blah = request.POST['usuarioId']
        dbLivro = Livros(titulo=livroTitulo, pagina=livroPage, obs=livroObs, usuario=User(blah))
        dbLivro.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse(template.render({}, request))
    

def delete_item(request, id):
    basicoLivro = Livros.objects.get(id=id)
    basicoLivro.delete()
    return HttpResponseRedirect('/')

def update_item(request, id):
    basicoLivroId = Livros.objects.get(id=id)
    basicoLivro = Livros.objects.all()
    context = {
        'basicoLivro':basicoLivro,
        'basicoLivroId':basicoLivroId,
    }
    if request.method =="POST":
        tituloUpdate = request.POST['livroTituloUpdate']
        paginasUpdate = request.POST['livroPageUpdate']
        obUpdate = request.POST['livroObsUpdate']
        basicoLivroId.titulo = tituloUpdate
        basicoLivroId.pagina = paginasUpdate
        basicoLivroId.obs = obUpdate
        basicoLivroId.save()
        return HttpResponseRedirect('/')
    else:
        template = loader.get_template('update.html')
        return HttpResponse(template.render(context,request))