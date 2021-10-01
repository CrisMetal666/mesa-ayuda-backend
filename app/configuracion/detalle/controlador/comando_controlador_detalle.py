from http import HTTPStatus

from flask import request, jsonify
from flask_jwt_extended import jwt_required

from app.comun.fabrica.fabrica_detalle import FabricaDetalle
from app.configuracion.detalle import detalle_bp
from app.configuracion.detalle.manejador.manejador_actualizar_detalle import ManejadorActualizarDetalle
from app.configuracion.detalle.repositorio.repositorio_detalle import RepositorioDetalle
from app.configuracion.detalle.servicio.servicio_actualizar_detalle import ServicioActualizarDetalle
from app.configuracion.detalle.servicio.servicio_crear_detalle import ServicioCrearDetalle
from app.seguridad.decoradores import admin_requerido
from app.configuracion.detalle.manejador.manejador_crear_detalle import ManejadorCrearDetalle

repositorio_detalle = RepositorioDetalle()
fabrica_detalle = FabricaDetalle()

servicio_crear_detalle = ServicioCrearDetalle(repositorio_detalle)
manejador_crear_detalle = ManejadorCrearDetalle(fabrica_detalle, servicio_crear_detalle)

servicio_actualizar_detalle = ServicioActualizarDetalle(repositorio_detalle)
manejador_actualizar_detalle = ManejadorActualizarDetalle(fabrica_detalle, servicio_actualizar_detalle)


@detalle_bp.route('/', methods=['POST'])
@jwt_required()
@admin_requerido
def crear():
    comando_detalle = request.get_json()
    respuesta = manejador_crear_detalle.ejecutar(comando_detalle)
    return jsonify(respuesta.__dict__), HTTPStatus.CREATED


@detalle_bp.route('/', methods=['PUT'])
@jwt_required()
@admin_requerido
def actualizar():
    comando_detalle = request.get_json()
    respuesta = manejador_actualizar_detalle.ejecutar(comando_detalle)
    return jsonify(respuesta.__dict__)
