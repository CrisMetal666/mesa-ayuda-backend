from app.comun.esquema.esquema_usuario_prueba import EsquemaUsuarioPrueba


class ManejadorListarUsuario:

    def __init__(self, dao_usuario):
        self.dao_usuario = dao_usuario

    def listar(self):
        esquema_usuario_prueba = EsquemaUsuarioPrueba(many=True)
        usuarios = self.dao_usuario.listar()
        return esquema_usuario_prueba.dump(usuarios)
