from app.comun.modelo.detalle import Detalle


class DaoDetalle:

    def obtener_por_maestro_id(self, maestro_id):
        return Detalle.query.filter_by(maestro_id=maestro_id) \
            .order_by(Detalle.valor, Detalle.habilitado.desc()).all()

    def obtener_por_id(self, id):
        return Detalle.query.get(id)
