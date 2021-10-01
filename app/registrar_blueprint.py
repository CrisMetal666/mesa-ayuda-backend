def registrar_blueprint(app):
    from app.seguridad import seguridad_bp
    app.register_blueprint(seguridad_bp)

    from app.configuracion import configuracion_bp
    app.register_blueprint(configuracion_bp)
