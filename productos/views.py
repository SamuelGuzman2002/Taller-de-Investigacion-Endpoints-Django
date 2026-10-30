
import json

from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Producto


@method_decorator(csrf_exempt, name='dispatch')
class ProductoView(View):

    def get(self, request, pk=None):
        if pk is not None:
            producto = get_object_or_404(Producto, pk=pk)
            return JsonResponse({
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'descripcion': producto.descripcion
            })

        productos = list(Producto.objects.values(
            'id', 'nombre', 'precio', 'descripcion'
        ))
        return JsonResponse({'productos': productos})

    def post(self, request):
        try:
            datos = json.loads(request.body)
            producto = Producto.objects.create(
                nombre=datos['nombre'],
                precio=datos['precio'],
                descripcion=datos.get('descripcion', '')
            )
            return JsonResponse({
                'mensaje': 'Producto creado correctamente',
                'id': producto.id
            }, status=201)
        except (ValueError, KeyError, TypeError) as error:
            return JsonResponse({'error': str(error)}, status=400)

    def put(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)

        try:
            datos = json.loads(request.body)
            producto.nombre = datos['nombre']
            producto.precio = datos['precio']
            producto.descripcion = datos.get('descripcion', '')
            producto.full_clean()
            producto.save()

            return JsonResponse({
                'mensaje': 'Producto actualizado correctamente'
            })
        except (ValueError, KeyError, TypeError) as error:
            return JsonResponse({'error': str(error)}, status=400)

    def delete(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()

        return JsonResponse({
            'mensaje': 'Producto eliminado correctamente'
        })
