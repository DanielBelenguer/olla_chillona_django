from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UsuarioPersonalizado,Plato,Descuento,Reserva,Menu,Servicio
from django.contrib.auth.hashers import make_password
from .forms import PlatoForm


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
        return render(request, 'restaurante/dashboard_jefe.html', {"l_descuentos": Descuento.objects.all()})
    if request.user.rol == 'cocinero':
        return render(request, 'restaurante/dashboard_cocinero.html')
    if request.user.rol == 'camarero':
        return render(request, 'restaurante/dashboard_camarero.html', {"l_reservas": Reserva.objects.all()})
    reservas_cliente = Reserva.objects.filter(usuario=request.user)
    servicios_finalizados = Servicio.objects.filter(usuario=request.user)
    return render(request, 'restaurante/dashboard_cliente.html', {
        "l_reservas": reservas_cliente,
        "saldo": request.user.saldo,
        "l_servicios": servicios_finalizados
    })


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

@login_required
def list_platos(request):
    l_platos = Plato.objects.all()
    return render(request, "restaurante/list_platos.html", {"l_platos": l_platos})

@login_required
def add_plato(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PlatoForm()
    return render(request, "restaurante/add_plato.html", {'form': form})

@login_required    
def detail(request, plato_id):
    plato = Plato.objects.get(id=plato_id)
    return render(request, "restaurante/detail.html", {"plato": plato})

@login_required
def edita_plato(request, plato_id):
    plato = Plato.objects.get(id=plato_id)
    if request.method == 'POST':
        plato.nombre = request.POST.get('nombre')
        plato.categoria = request.POST.get('categoria')
        plato.descripcion = request.POST.get('descripcion')
        plato.precio = float(request.POST.get('precio').replace(',', '.'))
        plato.save()
        return redirect('detail', plato_id=plato.id)
    return render(request, "restaurante/edita_plato.html", {"plato": plato})

@login_required
def add_descuento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        porcent = request.POST.get('porcent')
        Descuento.objects.create(nombre=nombre, porcent=porcent)
        l_descuentos = Descuento.objects.all()
        return render(request, "restaurante/dashboard_jefe.html", {"l_descuentos": l_descuentos})
    return render(request, "restaurante/add_descuento.html")


@login_required
def list_descuento(request):
    l_descuentos = Descuento.objects.all()
    return render(request, "restaurante/dashboard_jefe.html", {"l_descuentos": l_descuentos})


@login_required
def add_reserva(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        comensales = request.POST.get('comensales')
        Reserva.objects.create(fecha=fecha, hora=hora, num_personas=comensales, usuario=request.user)
        return redirect('dashboard')
    return render(request, "restaurante/add_reserva.html")


@login_required
def list_reserva(request):
    l_reservas = Reserva.objects.all()
    return render(request, "restaurante/dashboard_cliente.html", {"l_reservas": l_reservas})


@login_required
def add_saldo(request):
    if request.method == 'POST':
        saldo = request.POST.get('saldo')
        request.user.saldo += float(saldo)
        request.user.save()
        return redirect('dashboard')
    return render(request, "restaurante/add_saldo.html")


@login_required
def add_menu(request):
    l_platos = Plato.objects.all()
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        platos_ids = request.POST.getlist('platos')
        menu = Menu.objects.create(nombre=nombre, precio=precio)
        menu.platos.set(Plato.objects.filter(id__in=platos_ids))
    return render(request, 'restaurante/add_menu.html', {'l_platos': l_platos})


@login_required
def list_menus(request):
    l_menus = Menu.objects.all()
    return render(request, "restaurante/list_menus.html", {"l_menus": l_menus})

@login_required
def add_servicio(request, usuario_id):
    l_clientes = []
    l_platos = Plato.objects.all()
    l_menus = Menu.objects.all()
    usuario = None

    if usuario_id == 0:
        l_clientes = UsuarioPersonalizado.objects.filter(rol='cliente')
        reserva = False
    else:
        usuario = UsuarioPersonalizado.objects.get(pk=usuario_id)
        reserva = True

    if request.method == 'POST':
        menus_id = request.POST.getlist('menus')
        platos_id = request.POST.getlist('platos')
            
        serv = Servicio.objects.create(usuario=usuario)
        serv.platos.set(Plato.objects.filter(id__in=platos_id))
        serv.menus.set(Menu.objects.filter(id__in=menus_id))            
        serv.finalizado = True
        serv.save()
        total_servicio = 0
        for plato in serv.platos.all():
            total_servicio += plato.precio
        for menu in serv.menus.all():
            total_servicio += menu.precio
        serv.precio_total = total_servicio
        serv.save()

        return redirect('dashboard')
        
    return render(request, "restaurante/add_servicio.html", {'l_platos': l_platos, 'l_menus': l_menus, 'l_clientes': l_clientes})

@login_required
def pagar_servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)
    if request.method == 'POST':
        if request.user.saldo >= servicio.precio_total:
            request.user.saldo -= servicio.precio_total
            servicio.pagado = True
            request.user.save()
            servicio.save()
            messages.success(request, 'Servicio pagado con éxito.')
        else:
            precio_con_tarjeta = servicio.precio_total * 1.07
            request.user.saldo = 0
            servicio.pagado = True
            request.user.save()
            servicio.save()
        return redirect('dashboard')
    return render(request, 'restaurante/pagar_servicio.html', {"servicio": servicio})


@login_required
def historial_servicios(request):
    servicios = Servicio.objects.filter(usuario=request.user, pagado=True)
    return render(request, 'restaurante/historial_servicios.html', {"servicios": servicios})