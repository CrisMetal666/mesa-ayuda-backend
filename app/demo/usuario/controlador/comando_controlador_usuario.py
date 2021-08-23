from flask import request, jsonify

from app.demo.usuario import usuario_bp
from app.demo.usuario.fabrica.fabrica_usuario import FabricaUsuario
from app.demo.usuario.manejador.manejador_crear_usuario import ManejadorCrearUsuario
from app.demo.usuario.repositorio.repositorio_usuario import RepositorioUsuario
from app.demo.usuario.servicio.servicio_crear_usuario import ServicioCrearUsuario

repositorio_usuario = RepositorioUsuario()
fabrica_usuario = FabricaUsuario()
servicio_usuario = ServicioCrearUsuario(repositorio_usuario)
manejador_crear_usuario = ManejadorCrearUsuario(fabrica_usuario=fabrica_usuario,
                                                servicio_crear_usuario=servicio_usuario)


@usuario_bp.route('/', methods=['POST'])
def crear():
    comando_usuario = request.get_json()
    respuesta = manejador_crear_usuario.ejecutar(comando_usuario)
    return jsonify(respuesta.__dict__)
