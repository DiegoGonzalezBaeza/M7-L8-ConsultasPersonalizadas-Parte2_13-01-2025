from django.shortcuts import render
from .models import Pedidos, Productos, Usuarios  # Importa el modelo de tu tabla

def my_table_view(request):
    pedidos = Pedidos.objects.all()  # Realiza la consulta a la tabla
    productos = Productos.objects.all()
    usuarios = Usuarios.objects.all()
    return render(request, 'queries/my_table.html', {
        'pedidos': pedidos,
        'productos': productos,
        'usuarios': usuarios
    })