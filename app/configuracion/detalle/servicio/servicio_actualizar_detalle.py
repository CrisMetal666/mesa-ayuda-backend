from app.comun.excepciones import ExcepcionCampoInvalido


class ServicioActualizarDetalle:
    def __init__(self, repositorio_detalle):
        self.repositorio_detalle = repositorio_detalle

    def ejecutar(self, detalle):
        if not detalle.id:
            raise ExcepcionCampoInvalido('El detalle debe tener id')

        self.repositorio_detalle.guardar(detalle)
