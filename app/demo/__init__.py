from flask import Blueprint

from .usuario import usuario_bp

demo_bp = Blueprint('demo', __name__, url_prefix='/demo')
demo_bp.register_blueprint(usuario_bp)

