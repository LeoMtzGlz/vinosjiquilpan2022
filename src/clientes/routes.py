from flask import render_template, request, flash
import requests

from . import cliente

HOST = 'http://127.0.0.1:5000'

# Crear los endpoints
# Ruta: http://127.0.0.1:5000/clientes
@cliente.route('/registrar', methods=['GET', 'POST'])
def registrar_cliente():
    RUTA = '/api/clientes/registrar'
    URL = HOST + RUTA
    # Saber cual el metodo
    if request.method == 'POST':
        # Verificar que los datos no esten vacios
        if verificar_datos(request.form.to_dict()):
            # LLamado a la API
            respuesta = requests.post(URL, json = request.form.to_dict() )
            # print(respuesta.json())
            flash ( respuesta.json()['mensaje'])
        else:
            flash ( 'No se permiten valores vacios ')
    return render_template('/clientes/registro.html')

@cliente.route('/login', methods=['GET', 'POST'])
def login_cliente():
    RUTA = '/api/clientes/login'
    URL = HOST + RUTA
    # Saber cual el metodo
    if request.method == 'POST':
        # Verificar que los datos no esten vacios
        if verificar_datos(request.form.to_dict()):
            # LLamado a la API
            respuesta = requests.post(URL, json = request.form.to_dict() )
            # print(respuesta.json())
            flash ( respuesta.json()['mensaje'])
        # else:
        #     flash ( 'No se permiten valores vacios ')
    return render_template('/clientes/login.html')

def verificar_datos(datos):
    for indice, valor in datos.items():
        # print(indice, valor)
        if valor == '' or valor == None:
            return False
    return True
