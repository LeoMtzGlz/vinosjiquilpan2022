from flask import render_template
from src.db.mongodb import PyMongo
from . import producto

varmongo= {"host": "localhost",
           "db": "vinos_jiquilpan",
           "port": 27017,
           "timeout": 1000,
           "user": "",
           "password": ""
           }

# Crear los endpoints
# Ruta: http://127.0.0.1:5000/productos
@producto.route('/')
def index_productos(): # get_productos() idProducto, Nombre, Imagen
    # Abrir BAse de Datos
    objPyMongo = PyMongo(varmongo)
    # Consultar
    objPyMongo.conectar_mongodb()
    campos = {"_id":0,
              "idCategoria":1,
              "nombreCategoria":1,
              "imagenCategoria": 1}
    lista_categorias = objPyMongo.consulta_mongodb('categorias',{},campos)
    campos = {
        "_id": 0,
        "idProducto": 1,
        "productoNombreCorto": 1,
        "productoTipo": 1,
        "productoImagen": 1,
        "idCategoria.nombreCategoriaProducto": 1
    }
    lista_productos = objPyMongo.consulta_mongodb('productos', { 'productoTipo': {'$ne': 1} }, campos)
    # Cerrar la conexion
    objPyMongo.desconectar_mongodb()
    # Imprimir categorias
    print(lista_categorias)
    print(lista_productos)
    # Regresamos categorias
    return render_template('productos/index.html',
                           categorias = lista_categorias["resultado"],
                           productos = lista_productos["resultado"] ) # 'OK'

