from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.registrar_blueprint import registrar_blueprint
from app.registrar_excepciones import registrar_manejadores_errores

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()


def crear_aplicacion(modulo_configuracion):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_object(modulo_configuracion)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    registrar_blueprint(app)
    registrar_manejadores_errores(app)

    return app
