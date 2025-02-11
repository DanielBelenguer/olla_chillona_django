from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UsuarioPersonalizado,Plato,Descuento
from django.contrib.auth.hashers import make_password


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'restaurante/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'restaurante/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.rol == 'jefe':
        return render(request, 'restaurante/dashboard_jefe.html')
    if request.user.rol == 'cocinero':
        return render(request, 'restaurante/dashboard_cocinero.html')
    if request.user.rol == 'camarero':
        return render(request, 'restaurante/dashboard_camarero.html')
    return render(request, 'restaurante/dashboard_cliente.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        num_telefono = request.POST['num_telefono']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        rol = request.POST['rol']
        user = UsuarioPersonalizado.objects.create(username=username, nombre=nombre, apellidos=apellidos, num_telefono=num_telefono, email=email, password=password, rol=rol)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'restaurante/registro.html')

def list_platos(request):
    plato = Plato.objects.all()
    return render(request, "restaurante/list_platos.html", {"platos": plato})

def add_plato(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        Plato.objects.create(nombre=nombre, categoria=categoria, descripcion=descripcion, precio=precio)
    return render(request, "restaurante/add_plato.html")

    
def detail(request, plato_id):
    plato = Plato.objects.get(id=plato_id)
    return render(request, "restaurante/detail.html", {"plato": plato})

def edita_plato(request, plato_id):
    plato = Plato.objects.get(id=plato_id)
    if request.method == 'POST':
        plato.nombre = request.POST.get('nombre')
        plato.categoria = request.POST.get('categoria')
        plato.descripcion = request.POST.get('descripcion')
        plato.precio = request.POST.get('precio')
        plato.save()
        return redirect('detail', plato_id=plato.id)
    return render(request, "restaurante/editar_plato.html", {"plato": plato})

def crear_descuento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        porcentaje = request.POST.get('porcernaje')
        Descuento.objects.create(nombre=nombre, porcentaje=porcentaje)
    return render(request, "restaurante/crear_descuento.html")