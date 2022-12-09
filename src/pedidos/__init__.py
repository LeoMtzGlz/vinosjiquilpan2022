
from flask import Blueprint

# Definir el Blueprint
pedido = Blueprint('pedido', __name__, url_prefix='/pedidos', template_folder='templates')

# Le estamos diciendo Blueprint que tiene rutas definidas
from . import routes