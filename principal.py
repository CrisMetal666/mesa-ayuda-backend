import os

from app import crear_aplicacion

modulo_configuracion = os.getenv('APP_SETTING_MODULE')
app = crear_aplicacion(modulo_configuracion)
