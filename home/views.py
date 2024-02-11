from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from dashboard.models import Livros

# Create your views here.
def index(request):
    dblivros = Livros.objects.all()
    context = {
        'dblivros':dblivros
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))