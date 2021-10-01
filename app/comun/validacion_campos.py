from app.comun.excepciones import ExcepcionValorObligatorio, ExcepcionLongitudValor


def validar_obligatorio(valor, mensaje_error):
    if valor is None:
        raise ExcepcionValorObligatorio(mensaje_error)


def validar_longitud(valor, longitud, mensaje_error):
    validar_obligatorio(valor, 'El campo debe tener algun valor')
    if len(valor) > longitud:
        raise ExcepcionLongitudValor(mensaje_error)
