from django.shortcuts import render
import random
#Con esto podemos contener un texto que podemos mostrar
#from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'views/home.html')
def about(request):
    return render(request, 'views/about.html')
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    if(request.GET.get('uppercase')):
        #Añade a la lista characters estos caracteres en mayúsculas
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    #Se recorre la lista y se guarda el resultado de los valores escogidos 
    #aleatoriamente de la lista del abecedario
    for x in range(int(request.GET.get('length'))):
        generated_password += random.choice(characters)
    return render(request, 'views/password.html', {'password': generated_password})