# Investigación sobre Endpoints en Django Nativo

**Asignatura:** Desarrollo de Aplicaciones Web I  
**Docente:** José Javier Torres Vanstrahlen
**Estudiante:** Samuel Alfonso Guzmán Acevedo
**Tema:** Peticiones HTTP y operaciones CRUD en Django

## 1. Introducción

En esta investigación estuve revisando cómo se pueden crear endpoints utilizando Django, sin necesidad de instalar otras librerías como Django REST Framework.

Django es un framework que trabaja con Python y que nos permite desarrollar aplicaciones web. Algo que me pareció interesante es que ya trae varias herramientas con las que podemos recibir peticiones, procesar información y devolver respuestas.

La idea de este trabajo es conocer cómo funcionan los métodos GET, POST, PUT y DELETE, para qué sirve cada uno y cómo se relacionan con las operaciones CRUD.

También realicé un pequeño proyecto de productos para poner en práctica lo investigado y comprobar que los cuatro métodos funcionaran.

## 2. ¿Qué es un endpoint?

Por lo que estuve investigando, un endpoint es básicamente una dirección URL que permite comunicarnos con una aplicación para solicitar o enviar información.

Por ejemplo, en el proyecto que desarrollé utilicé esta dirección:

`http://127.0.0.1:8000/api/productos/`

Cuando ingresamos a esa dirección podemos consultar los productos que tenemos guardados, pero también podemos utilizarla para registrar productos nuevos dependiendo del tipo de petición que enviemos.

En Django esto se maneja principalmente desde dos archivos:

- `urls.py`: donde definimos las direcciones o rutas.
- `views.py`: donde escribimos lo que debe hacer el programa cuando recibe una petición.

## 3. ¿Cómo crear endpoints en Django nativo?

Una de las cosas que encontré es que Django permite trabajar con endpoints sin utilizar Django REST Framework, ya que cuenta con sus propias clases y funciones para manejar las solicitudes HTTP.

Para crear un endpoint básico necesitamos definir una ruta y una vista que se encargue de recibir la petición.

Algunas de las herramientas que encontré fueron:

- **View:** nos permite crear vistas basadas en clases y manejar diferentes métodos HTTP.
- **JsonResponse:** sirve para devolver información en formato JSON.
- **path():** permite definir las rutas de nuestra aplicación.
- **as_view():** se utiliza para conectar una vista basada en clase con una URL.
- **HttpRequest:** representa la petición que recibe Django.

El funcionamiento es relativamente sencillo. Cuando hacemos una petición a una URL, Django busca la ruta correspondiente y ejecuta el método que tenga definido la vista.

Por ejemplo, si enviamos una petición GET, Django ejecuta el método `get()` de nuestra clase.

## 4. Métodos HTTP y operaciones CRUD

Los métodos HTTP son los que permiten indicar qué acción queremos realizar sobre la información.

Estos métodos se pueden relacionar con CRUD, que significa Create, Read, Update y Delete. En español sería crear, leer, actualizar y eliminar.

| Método | CRUD | ¿Para qué sirve? |
|---|---|---|
| GET | Read | Consultar información |
| POST | Create | Registrar información nueva |
| PUT | Update | Actualizar información existente |
| DELETE | Delete | Eliminar información |

### 4.1. Método GET

GET se utiliza cuando queremos consultar información.

Por ejemplo, si tenemos varios productos guardados en una base de datos, podemos utilizar GET para obtener la lista completa o consultar uno en específico.

En mi proyecto lo utilicé para mostrar los productos registrados.

**Ejemplo:**

`GET /api/productos/`

Al ingresar desde el navegador, Django devuelve la información en formato JSON.

### 4.2. Método POST

POST sirve para enviar información al servidor, normalmente para crear un registro nuevo.

En el proyecto lo utilicé para registrar un producto con su nombre, precio y descripción.

**Ejemplo:**

`POST /api/productos/`

Para probarlo envié los datos de un perfume desde PowerShell y el sistema lo guardó en la base de datos.

Cuando el producto se crea correctamente, Django devuelve una respuesta con el código 201, que indica que el registro fue creado.

### 4.3. Método PUT

PUT se utiliza para actualizar la información de un recurso que ya existe.

Por ejemplo, si registramos un producto con un precio y después necesitamos cambiarlo, podemos utilizar este método.

**Ejemplo:**

`PUT /api/productos/1/`

En este caso el número 1 corresponde al ID del producto que queremos modificar.

Durante las pruebas cambié el nombre y el precio de un producto que ya había registrado, y después comprobé con GET que los cambios se habían guardado.

### 4.4. Método DELETE

DELETE permite eliminar un registro existente.

Para utilizarlo necesitamos identificar cuál es el recurso que queremos borrar.

**Ejemplo:**

`DELETE /api/productos/1/`

En mi proyecto lo probé eliminando el producto que había creado anteriormente.

Después volví a consultar la lista de productos y pude comprobar que ya no aparecía.

## 5. Vistas basadas en clases

Otra parte importante de la investigación fueron las vistas basadas en clases.

Django tiene una clase llamada `View` que nos permite organizar los diferentes métodos HTTP dentro de una misma clase.

Esto me pareció útil porque no tenemos que crear una función completamente separada para cada petición, sino que podemos manejar las operaciones de un recurso desde una misma clase.

En el proyecto utilicé una estructura como esta:

```python
class ProductoView(View):

    def get(self, request, pk=None):
        ...

    def post(self, request):
        ...

    def put(self, request, pk):
        ...

    def delete(self, request, pk):
        ...
```

Cada método tiene una función diferente dependiendo de la petición que reciba Django.

También encontré que Django utiliza un mecanismo llamado `dispatch()`, que se encarga de identificar el método HTTP y dirigir la petición al método correspondiente de la clase.

## 6. Módulos, funciones y decoradores utilizados

Para desarrollar los endpoints estuve revisando algunas herramientas que Django ya tiene incluidas.

Estas fueron las principales que utilicé en el proyecto:

| Elemento | Módulo | Función |
|---|---|---|
| View | django.views | Permite crear vistas basadas en clases |
| JsonResponse | django.http | Devuelve respuestas en formato JSON |
| path | django.urls | Define las rutas de la aplicación |
| include | django.urls | Permite incluir rutas de otra aplicación |
| get_object_or_404 | django.shortcuts | Busca un registro y devuelve error 404 si no existe |
| csrf_exempt | django.views.decorators.csrf | Desactiva la verificación CSRF de una vista |
| method_decorator | django.utils.decorators | Permite aplicar decoradores a métodos o clases |
| models.Model | django.db.models | Se utiliza para crear modelos de base de datos |
| as_view | View | Permite conectar una vista basada en clase con una URL |

También utilicé `json.loads()`, que pertenece al módulo `json` de Python. Esta función permite convertir los datos JSON recibidos en información que podamos manejar desde el código.

Algo importante que encontré es que `csrf_exempt` desactiva una protección de seguridad de Django. En este ejercicio lo utilicé para poder hacer las pruebas de POST, PUT y DELETE de manera más sencilla.

Sin embargo, en un proyecto real no sería recomendable dejar los endpoints sin las protecciones necesarias, especialmente si se manejan datos de usuarios.

## 7. Desarrollo práctico

Para entender mejor lo investigado decidí realizar una aplicación sencilla de productos utilizando Django y SQLite.

La aplicación se llama `productos` y permite registrar, consultar, actualizar y eliminar información.

Primero creé el proyecto de Django y después la aplicación donde iba a trabajar.

Luego configuré el modelo Producto con tres campos principales:

- **nombre:** para guardar el nombre del producto.
- **precio:** para almacenar su valor.
- **descripcion:** para agregar información adicional.

Después realicé las migraciones para que Django creara la tabla correspondiente en la base de datos.

Las rutas que utilicé fueron:

| Ruta | Métodos |
|---|---|
| `/api/productos/` | GET y POST |
| `/api/productos/<int:pk>/` | GET, PUT y DELETE |

Los archivos que trabajé fueron:

- `models.py`: donde definí los datos del producto.
- `views.py`: donde programé los cuatro métodos HTTP.
- `urls.py`: donde configuré las rutas.
- `settings.py`: donde registré la aplicación.

Para este desarrollo no utilicé Django REST Framework, ya que la intención era trabajar con las herramientas que Django trae de manera nativa.

## 8. Pruebas de funcionamiento

Después de terminar el código realicé varias pruebas para comprobar que los endpoints estuvieran funcionando.

Primero inicié el servidor de Django con el comando `python manage.py runserver`.

**Prueba GET**

Ingresé desde el navegador a la dirección:

`http://127.0.0.1:8000/api/productos/`

Al principio apareció una lista vacía porque todavía no había registrado ningún producto.

La respuesta fue:

```json
{
    "productos": []
}
```

**Prueba POST**

Después utilicé PowerShell para enviar una petición POST con estos datos:

- Nombre: Perfume
- Precio: 35000
- Descripción: Perfume de 100 ml

El sistema respondió que el producto había sido creado correctamente.

Al actualizar la página del navegador pude ver que el producto ya estaba registrado.

**Prueba PUT**

Para comprobar PUT modifiqué el producto que había creado.

Cambié los datos por:

- Nombre: Perfume Premium
- Precio: 50000
- Descripción: Perfume premium de 100 ml

El sistema mostró el mensaje de actualización y al consultar nuevamente el producto pude comprobar que los datos habían cambiado.

**Prueba DELETE**

Por último utilicé DELETE para eliminar el producto registrado.

Después consulté nuevamente el endpoint y la lista volvió a aparecer vacía, lo que confirmó que el producto había sido eliminado.

Con estas pruebas pude comprobar cómo funcionan las cuatro operaciones CRUD desde Django.

## 9. ¿Cómo ejecutar el proyecto?

Para ejecutar el proyecto es necesario tener instalado Python y Django.

Primero instalamos Django desde la terminal:

```bash
python -m pip install django
```

Después aplicamos las migraciones:

```bash
python manage.py migrate
```

Luego iniciamos el servidor:

```bash
python manage.py runserver
```

Una vez que el servidor esté funcionando podemos ingresar a:

`http://127.0.0.1:8000/api/productos/`

Desde el navegador podemos probar GET, mientras que para los otros métodos podemos utilizar PowerShell o alguna herramienta como Postman.

## 10. Conclusiones

Con esta investigación pude entender mejor cómo funcionan los endpoints y cómo podemos utilizarlos dentro de una aplicación desarrollada en Django.

Antes de realizar el ejercicio no tenía tan claro cómo se relacionaban los métodos HTTP con las operaciones CRUD, pero al trabajar con el ejemplo de productos pude comprender mejor para qué sirve cada uno.

También aprendí que no siempre necesitamos instalar librerías adicionales para crear una API sencilla, porque Django ya cuenta con herramientas como `View`, `JsonResponse` y las funciones para manejar las rutas.

Otra cosa que me quedó más clara fue la importancia de los archivos `views.py` y `urls.py`, ya que uno se encarga de manejar las peticiones y el otro de definir las direcciones por donde podemos acceder a ellas.

En general, este trabajo me sirvió para practicar el manejo de peticiones HTTP y entender un poco más cómo se comunica una aplicación con el servidor y la base de datos.

## 11. Fuentes de consulta

Para realizar la investigación tomé como referencia la documentación oficial de Django y la información de MDN sobre los métodos HTTP.

- Django Software Foundation. Class-based views: https://docs.djangoproject.com/en/6.0/topics/class-based-views/
- Django Software Foundation. Base views: https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/
- Django Software Foundation. Request and response objects: https://docs.djangoproject.com/en/6.0/ref/request-response/
- Django Software Foundation. URL dispatcher: https://docs.djangoproject.com/en/6.0/topics/http/urls/
- Django Software Foundation. Django shortcut functions: https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/
- Django Software Foundation. View decorators: https://docs.djangoproject.com/en/6.0/topics/http/decorators/
- MDN Web Docs. HTTP request methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
