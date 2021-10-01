from flask import Blueprint

from .detalle import detalle_bp
from .maestro import maestro_bp

configuracion_bp = Blueprint('configuracion', __name__, url_prefix='/configuracion')
configuracion_bp.register_blueprint(maestro_bp)
configuracion_bp.register_blueprint(detalle_bp)
