from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.seguridad.inicio_sesion import inicio_sesion_bp
from app.seguridad.decoradores import admin_requerido
from app.seguridad.inicio_sesion.dao.dao_inicio_sesion import DaoInicioSesion
from app.seguridad.inicio_sesion.servicio.servicio_inicio_sesion import ServicioInicioSesion

dao_iniciar_sesion = DaoInicioSesion()
servicio_iniciar_sesion = ServicioInicioSesion(dao_iniciar_sesion)


@inicio_sesion_bp.route('/generar-token', methods=["POST"])
def login():
    usuario = request.json.get('usuario', None)
    clave = request.json.get('clave', None)
    token = servicio_iniciar_sesion.ejecutar(usuario, clave)
    return jsonify(token=token)


@inicio_sesion_bp.route("/protected", methods=["GET"])
@jwt_required()
@admin_requerido
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
