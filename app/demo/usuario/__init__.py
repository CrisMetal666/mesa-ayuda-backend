from flask import Blueprint

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')

# from . import routes
from .controlador import comando_controlador_usuario
from .controlador import consulta_controlador_usuario
