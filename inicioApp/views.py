from django.contrib import messages
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from inicioApp.forms import *
from .models import *


def inicioDef(request):
    return render(request, 'inicio.html', {})

def loginSesionDef(request):
    if request.method == 'GET':
        return render(request, 'inicio.html', {})
    else:
        usuarioStr = request.POST.get('userIntx')
        passswordStr = request.POST.get('passwordInPs')
        try:
             print(usuarioStr,passswordStr)
             usuario = Usuario.objects.get(usuario=usuarioStr, password=passswordStr)
             print(usuarioStr, passswordStr)
             return render(request, "menu.html", {"usuarioStr":usuario.usuario})
        except Usuario.DoesNotExist:
            return render(request,"inicio.html",{"err":"Usuario o contraseña no son correctos"})

def registrarusuario(request):
    usuario = request.POST['txtusuario']
    password = request.POST['setpassword']

    usuario1 = Usuario.objects.create(
        usuario=usuario, password=password )
    messages.success(request, '¡Usuario registrado!')
    return redirect('inicioUrl')

def ClientesDef(request):
    Clientes: QuerySet[cliente] = cliente.objects.all()
    form_personal = Clienteform()
    context ={
        'Clientes':Clientes,
        'form_personal' : form_personal

    }
    return render(request, 'Clientes.html', context)


def add_ClientesDef(request):
    if request.POST:
        form = Clienteform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"Error al guardar")
                return redirect('Clientes')
    return redirect('Clientes')

def add_PedicureDef(request):
    if request.POST:
        form = Manicureform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"Error al guarder")
                return redirect('Pedicure')
    return redirect('Pedicure')
def PedicureDef(request):
    D_Pedicure: QuerySet[manicure] = manicure.objects.all()
    form_personal = Manicureform()
    context ={
        'D_Pedicure':D_Pedicure,
        'form_personal' : form_personal

    }
    return render(request, 'Pedicure.html', context)





def ManicureDef(request):
    Manicure_v = manicure.objects.all()
    form_personal = Pedicureform()
    context ={
        'Manicure_D':Manicure_v,
        'form_personal' : form_personal

    }
    return render(request, 'Manicure.html', context)


def add_ManicureDef(request):
    #print('GUARDAR CLIENTE')
    if request.POST:
        form = Manicureform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"Error al guardar")
                return redirect('Manicure')
    return redirect('Manicure')