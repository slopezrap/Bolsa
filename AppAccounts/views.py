from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import FormularioUserLogin,FormularioUserRegister 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def VistaSignUp(request):
    if request.method == "GET":
        logout(request)
        return redirect(reverse('name-NoFuncionalidad')) 
   
    
    
def VistaLogin(request):
    if request.method == "GET":
        template = "AppAccounts/Login.html"
        nombre_pestania = "Login"
        formulario = FormularioUserLogin()
        contexto = {
            "clave_nombre_pestania" : nombre_pestania,
            'clave_formulario_template': formulario,
        }         
        return render(request, template , contexto)  
    
    if request.method == "POST":
        formulario = FormularioUserLogin(request.POST)
        if formulario.is_valid(): 
            #Uso formulario.cleaned_data.get en lugar de request.POST.get porque el primero chequea la condicion del formulario
            username = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request,user)
            #print(request.user.is_authenticated)
            return redirect(reverse('name-home')) 
        else:
            template = "AppAccounts/Login.html"
            nombre_pestania = "Login"
            contexto = {
                "clave_nombre_pestania" : nombre_pestania,
                'clave_formulario_template': formulario,
            }         
            return render(request, template , contexto)  

def VistaLogout(request):
    if request.method == "GET":
        logout(request)
        return redirect(reverse('name-home')) 


