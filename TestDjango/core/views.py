from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import stockForm
from .forms import compraForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def perro(request):
    return render(request, 'core/perro.html')

def gatos(request):
    return render(request, 'core/gatos.html')

def aves(request):
    return render(request, 'core/aves.html')

def descuentos(request):
    return render(request, 'core/descuentos.html')

def suscribirse(request):
    return render(request, 'core/suscribirse.html')


def productos(request):
    stocks= stock.objects.all()
    return render(request, 'core/productos.html', {'contexto':stocks})

def eliminarproducto(request, id):
    stocks = stock.objects.get(cod=id)
    stocks .delete()
    return redirect(to = "productos")

def modificar(request, id):
    promociones = stock.objects.get(cod=id)
    datos = {'form': stockForm(instance=promociones)}
    if request.method == "POST":
        form = stockForm(request.POST, instance=promociones)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/modificar.html', datos)



def pagar(request):
    carro= compra.objects.all()
    return render(request, 'core/pagar.html', {'contexto':carro})



def carrito(request):
    carro= compra.objects.all()
    return render(request, 'core/carrito.html', {'contexto':carro})



def cancelar(request, id):
    carro = compra.objects.get(compra=id)
    carro .delete()
    return redirect(to = "compras")

def modificarcompra(request, id):
    promociones = compraForm.objects.get(compra=id)
    datos = {'form': compraForm(instance=promociones)}
    if request.method == "POST":
        form = compraForm(request.POST, instance=promociones)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/modificarcompra.html', datos)


    
def inicio(request):
    return render(request, 'core/inicio.html')

def crear(request):
    return render(request, 'core/crear.html')

def compras(request):
    return render(request, 'core/compras.html')

def agregar(request):
    return render(request, 'core/agregar.html')

def crearproducto(request):
    datos = {"form":stockForm()}
    if request.method == "POST":
        form = stockForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Agregado"
    return render(request, 'core/crearproducto.html', datos)


def pagar(request):
    datos = {"form":compraForm()}
    if request.method == "POST":
        form = compraForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Agregado"
    return render(request, 'core/pagar.html', datos)




def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="registro")
    return render(request, 'core/registro.html', {'form':form})

 