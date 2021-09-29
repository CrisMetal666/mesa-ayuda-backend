from flask import Blueprint

inicio_sesion_bp = Blueprint('inicio_sesion', __name__, url_prefix='/inicio-sesion')

from .controlador import consulta_controlador_inicio_sesion