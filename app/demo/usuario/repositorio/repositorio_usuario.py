from app import db
from app.comun.modelo.usuario_prueba import UsuarioPrueba


class RepositorioUsuario:

    def crear(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario.id

    def buscar_por_id(self, id):
        return UsuarioPrueba.query.get(id)
