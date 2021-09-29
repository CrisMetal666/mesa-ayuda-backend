import traceback
from http import HTTPStatus

from app.comun.excepciones import ExcepcionEntidadNoEncontrada, ExcepcionValorObligatorio, \
    ExcepcionCredencialesIncorrectas
from app.comun.excepciones import ExcepcionSinAutorizacion


def registrar_manejadores_errores(app):
    @app.errorhandler(ExcepcionEntidadNoEncontrada)
    def manejar_excepcion_entidad_no_encontrada(e):
        return armar_mensaje_error(e, HTTPStatus.NOT_FOUND)

    @app.errorhandler(ExcepcionValorObligatorio)
    def manejar_excepcion_entidad_no_encontrada(e):
        return armar_mensaje_error(e, HTTPStatus.BAD_REQUEST)

    @app.errorhandler(ExcepcionSinAutorizacion)
    def manejar_excepcion_sin_autorizacion(e):
        return armar_mensaje_error(e, HTTPStatus.UNAUTHORIZED)

    @app.errorhandler(ExcepcionCredencialesIncorrectas)
    def manejar_excepcion_sin_autorizacion(e):
        return armar_mensaje_error(e, HTTPStatus.BAD_REQUEST)


def armar_mensaje_error(e, http_status):
    traceback.print_tb(e.__traceback__)
    return {'mensaje': str(e)}, http_status
