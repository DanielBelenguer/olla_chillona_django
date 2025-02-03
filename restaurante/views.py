from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UsuarioPersonalizado
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
    return render(request, 'restaurante/dashboard_empleado.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        rol = request.POST['rol']
        user = UsuarioPersonalizado.objects.create(username=username, email=email, password=password, rol=rol)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'restaurante/registro.html')
