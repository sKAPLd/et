from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
#pip install request
import requests
# Create your views here.


def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
        
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    if suscrito:
        venta.total = total * .95
    venta.save()
    for item in carro:
        producto = Producto.objects.get(codigo = item[0])
        detalle = DetalleVenta()
        detalle.producto = producto
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        producto.stock = producto.stock - item[4]
        producto.save()
        request.session["carro"] = []

    return redirect(to="carrito")



def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo :
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")




def carrito(request):
    context ={}
    carro = request.session.get("carro", [])
    suscrito(request, context)
    context["carro"] = carro

    return render(request, 'core/carrito.html', context)

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo :
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
            carro.append([codigo, producto.detalle , producto.imagen , producto.precio, 1, producto.precio ])
    request.session["carro"] = carro
    return redirect(to="home")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")

def home(request):
    accesorios = Producto.objects.all()
    context = {'accesorios': accesorios}
    suscrito(request, context)
    print(context)
    return render(request, 'core/index.html', context )

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]


def login(request):
    return render(request, 'core/login.html')


def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html',{'form':registro})

def subs(request):
    return render(request, 'core/Suscripciones.html')

def suscribirme(request):
    context = {}

    if request.method == "POST":  
       if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
       return render(request, 'core/Suscripciones.html', context)
    else:
        suscrito(request, context)

        return render(request, 'core/Suscripciones.html', context)


    
def catalogo(request):
    return render(request, 'core/Productos.html')

def logout(request):
    return logout_then_login(request, login_url="login")

def contacto(request):
    return render(request, 'core/contacto.html')

def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    ventas = Venta.objects.filter(cliente=request.user)
    return render(request, 'core/historial.html', {"ventas":ventas})

def adminproducto(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
        
    return render(request, 'core/C_productos.html')

def adminC(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
        
    return render(request, 'core/C.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')




