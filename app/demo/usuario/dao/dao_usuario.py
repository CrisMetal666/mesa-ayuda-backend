from app.comun.modelo.usuario_prueba import UsuarioPrueba


class DaoUsuario:

    def listar(self):
        return UsuarioPrueba.query.all()
