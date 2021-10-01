from app import db


class RepositorioDetalle:

    def guardar(self, detalle):
        db.session.add(detalle)
        db.session.commit()
        return detalle.id
