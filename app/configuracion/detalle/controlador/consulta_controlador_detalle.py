from flask import jsonify
from flask_jwt_extended import jwt_required

from app.configuracion.detalle import detalle_bp
from app.configuracion.detalle.dao.dao_detalle import DaoDetalle
from app.configuracion.detalle.servicio.servicio_consultar_por_id import ServicioConsultarPorId
from app.configuracion.detalle.servicio.servicio_consultar_por_maestro import ServicioConsultarPorMaestro
from app.seguridad.decoradores import admin_requerido

dao_detalle = DaoDetalle()
servicio_consultar_por_maestro = ServicioConsultarPorMaestro(dao_detalle)
servicio_consultar_por_id = ServicioConsultarPorId(dao_detalle)


@detalle_bp.route('/<maestro_id>/maestro')
@jwt_required()
@admin_requerido
def obtener_por_maestro_id(maestro_id):
    return jsonify(servicio_consultar_por_maestro.ejecutar(maestro_id))


@detalle_bp.route('/<id>')
@jwt_required()
@admin_requerido
def obtener_por_id(id):
    return jsonify(servicio_consultar_por_id.ejecutar(id))
