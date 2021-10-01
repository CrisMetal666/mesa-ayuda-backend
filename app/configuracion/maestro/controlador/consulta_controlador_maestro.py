from flask import jsonify
from flask_jwt_extended import jwt_required

from app.configuracion.maestro import maestro_bp
from app.configuracion.maestro.dao.dao_maestro import DaoMaestro
from app.configuracion.maestro.servicio.servicio_consultar_editable import ServicioConsultarEditable
from app.seguridad.decoradores import admin_requerido

dao_maestro = DaoMaestro()
servicio_consultar_editable = ServicioConsultarEditable(dao_maestro)


@maestro_bp.route('/editable')
@jwt_required()
@admin_requerido
def obtener_maestro_editable():
    resultado = servicio_consultar_editable.ejecutar()
    return jsonify(resultado)
