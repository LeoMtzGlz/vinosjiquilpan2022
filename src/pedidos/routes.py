from flask import render_template, request

from . import pedido

# Crear los endpoints
# Ruta: http://127.0.0.1:5000/productos
@pedido.route('/carrito')
def ver_carrito():
    return render_template('/pedidos/carrito.html')

@pedido.route('/checkout')
def verificar_cuenta():
    return 'Desde Cuenta . . .'



