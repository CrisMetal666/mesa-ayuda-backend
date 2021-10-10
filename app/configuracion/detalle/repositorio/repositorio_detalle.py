from app import db
from app.comun.modelo.detalle import Detalle


class RepositorioDetalle:

    def guardar(self, detalle):
        if detalle.id is None:
            db.session.add(detalle)
        db.session.commit()
        return detalle.id

    def buscar_por_id(self, id):
        return Detalle.query.get(id)
