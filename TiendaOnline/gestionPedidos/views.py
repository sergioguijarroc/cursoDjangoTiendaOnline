from django.http import HttpResponse
from django.shortcuts import render

from gestionPedidos.models import Articulos

# Create your views here.


def busqueda_productos(request):
    return render(request, "gestionPedidos/busqueda_productos.html")


def buscar(request):
    if request.GET["prd"]:
        # mensaje = f"Artículo buscado: {request.GET['prd']}"
        producto = request.GET["prd"]
        if len(producto) > 20:
            mensaje = "Texto de búsqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(
                nombre__icontains=producto
            )  # El icontains es como un like en SQL, muestra todos los que coinciden parcialmente con ese nombre de producto
            return render(
                request,
                "gestionPedidos/resultados_busqueda.html",
                {"articulos": articulos, "query": producto},
            )
    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)
