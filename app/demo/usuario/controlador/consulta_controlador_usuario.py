from flask import jsonify

from app.demo.usuario import usuario_bp
from app.demo.usuario.dao.dao_usuario import DaoUsuario
from app.demo.usuario.manejador.manejador_listar_usuario import ManejadorListarUsuario

dao_usuario = DaoUsuario()
manejador_listar_usuario = ManejadorListarUsuario(dao_usuario)


@usuario_bp.route('/', methods=['GET'])
def listar():
    return jsonify(manejador_listar_usuario.listar())
