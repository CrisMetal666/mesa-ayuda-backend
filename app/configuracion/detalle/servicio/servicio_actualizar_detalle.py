from app.comun.excepciones import ExcepcionCampoInvalido, ExcepcionEntidadNoEncontrada


class ServicioActualizarDetalle:
    MENSAJE_DETALLE_SIN_ID = 'El detalle debe tener id'
    MENSAJE_ENTIDAD_NO_ENCONTRADA = 'El detalle no existe'

    def __init__(self, repositorio_detalle):
        self.repositorio_detalle = repositorio_detalle

    def ejecutar(self, detalle):
        modelo = self._consultar_y_validar_por_id(detalle.id)
        self._setear_datos_al_modelo(modelo, detalle)
        self.repositorio_detalle.guardar(modelo)
        return modelo

    def _consultar_y_validar_por_id(self, id):
        if id is None:
            raise ExcepcionCampoInvalido(self.MENSAJE_DETALLE_SIN_ID)

        entidad = self.repositorio_detalle.buscar_por_id(id)

        if entidad is None:
            raise ExcepcionEntidadNoEncontrada(self.MENSAJE_ENTIDAD_NO_ENCONTRADA)

        return entidad

    def _setear_datos_al_modelo(self, modelo, detalle):
        modelo.valor = detalle.valor
        modelo.maestro_id = detalle.maestro_id
        modelo.habilitado = detalle.habilitado
        modelo.usuario_id = detalle.usuario_id
