from flask import Blueprint

detalle_bp = Blueprint('detalle', __name__, url_prefix='/detalle')

from .controlador import consulta_controlador_detalle
from .controlador import comando_controlador_detalle
