from flask import Blueprint

from .inicio_sesion import inicio_sesion_bp

seguridad_bp = Blueprint('seguridad', __name__, url_prefix='/seguridad')
seguridad_bp.register_blueprint(inicio_sesion_bp)
