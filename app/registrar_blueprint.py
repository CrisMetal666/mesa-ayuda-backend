def registrar_blueprint(app):
    from app.demo import demo_bp
    app.register_blueprint(demo_bp)

    from app.seguridad import seguridad_bp
    app.register_blueprint(seguridad_bp)
