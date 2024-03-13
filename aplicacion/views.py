from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def catalogo(request):
    telefonos = Telefonos.objects.all()
    cargadores = Cargadores.objects.all()
    accesorios = Accesorios.objects.all()
    return render(request, 'index.html', {'telefonos': telefonos,'cargadores':cargadores,'accesorios':accesorios})

def buscar(request):
    query = request.GET.get('q')
    telefonos = Telefonos.objects.filter(nombre__icontains=query)
    cargadores = Cargadores.objects.filter(nombre__icontains=query)
    accesorios = Accesorios.objects.filter(nombre__icontains=query)
    return render(request, 'buscar.html', {'telefonos': Telefonos,'cargadores':Cargadores,'Accesorios':Accesorios})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})
# Create your views here.
