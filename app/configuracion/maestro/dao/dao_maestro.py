from app.comun.modelo.maestro import Maestro


class DaoMaestro:

    def obtener_editables(self):
        return Maestro.query.filter_by(editable=True).all()
