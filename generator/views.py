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
    #Lista de caracteres con las letras del abecedario
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    #Si selecciona el checkbox uppercase entonces
    if(request.GET.get('uppercase')):
        #Añade a la lista characters estos caracteres en mayúsculas
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    #Condición para caracteres especiales
    if(request.GET.get('special')):
        characters.extend(list('!@#$%&*^[]()'))
    #Condición para números
    if(request.GET.get('numbers')):
        characters.extend(list('0123456789'))    
    #Se recorre la lista y se guarda el resultado de los valores escogidos 
    #aleatoriamente de la lista del abecedario
    for x in range(int(request.GET.get('length'))):
        generated_password += random.choice(characters)
    #Renderiza la vista html y la variable password toma el valor de generated_password
    return render(request, 'views/password.html', {'password': generated_password})