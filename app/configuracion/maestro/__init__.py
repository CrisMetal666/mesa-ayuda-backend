from flask import Blueprint

maestro_bp = Blueprint('maestro', __name__, url_prefix='/maestro')

from .controlador import consulta_controlador_maestro