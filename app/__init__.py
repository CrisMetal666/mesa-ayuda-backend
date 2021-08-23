import traceback
from http import HTTPStatus

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.comun.excepciones import ExcepcionEntidadNoEncontrada, ExcepcionValorObligatorio

db = SQLAlchemy()
ma = Marshmallow()


def crear_aplicacion(modulo_configuracion):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(modulo_configuracion)

    db.init_app(app)
    ma.init_app(app)

    registrar_blueprint(app)
    registrar_manejadores_errores(app)

    return app


def registrar_blueprint(app):
    from app.demo import demo_bp
    app.register_blueprint(demo_bp)


def registrar_manejadores_errores(app):
    @app.errorhandler(ExcepcionEntidadNoEncontrada)
    def manejar_excepcion_entidad_no_encontrada(e):
        return armar_mensaje_error(e, HTTPStatus.NOT_FOUND)

    @app.errorhandler(ExcepcionValorObligatorio)
    def manejar_excepcion_entidad_no_encontrada(e):
        return armar_mensaje_error(e, HTTPStatus.BAD_REQUEST)


def armar_mensaje_error(e, http_status):
    traceback.print_tb(e.__traceback__)
    return {'msg': str(e)}, http_status
