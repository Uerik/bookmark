from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.template import loader
from django.contrib.auth.models import User

# Create your views here.
def login_usuario(request):
    if request.method == 'POST':
        usuarioLogin = request.POST['loginUsuario']
        usuarioSenha = request.POST['senhaUsuario']
        usuario = authenticate(request, username=usuarioLogin, password=usuarioSenha)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('<h1>Erro ao logar</h1>')


def cadastro_usuario(request):
    template = loader.get_template('cadastro.html')
    if request.method == 'POST':
        usuario_login = request.POST['loginUsuarioCadastro']
        usuario_senha = request.POST['senhaUsuarioCadastro']
        usuario = User.objects.create_user(username=usuario_login, password=usuario_senha,)
        usuario.save()
        usuario = authenticate(request, username=usuario_login, password=usuario_senha)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/')
    return HttpResponse(template.render({}, request))


def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/')