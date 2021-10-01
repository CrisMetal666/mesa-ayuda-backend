from app.comun.modelo.detalle import Detalle


class FabricaDetalle:
    def crear(self, comando_detalle):
        detalle = Detalle(
            id=comando_detalle['id'],
            valor=comando_detalle['valor'],
            maestro_id=comando_detalle['maestro_id'],
            habilitado=comando_detalle['habilitado'],
            usuario_id=comando_detalle['usuario_id']
        )

        return detalle
