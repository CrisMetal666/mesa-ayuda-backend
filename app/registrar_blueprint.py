def registrar_blueprint(app):
    from app.seguridad import seguridad_bp
    app.register_blueprint(seguridad_bp)
