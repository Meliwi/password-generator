from django.shortcuts import render
#Con esto podemos contener un texto que podemos mostrar
#from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'views/home.html')
def about(request):
    return render(request, 'views/about.html')