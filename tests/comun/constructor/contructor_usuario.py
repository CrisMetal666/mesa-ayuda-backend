from app.comun.modelo.usuario import Usuario


class ConstructorUsuario:
    campo_id = 1
    campo_persona_id = 1
    campo_clave = ''
    campo_habilitado = True
    campo_usuario_id = 1

    @classmethod
    def id(cls, id):
        cls.campo_id = id
        return cls

    @classmethod
    def persona_id(cls, persona_id):
        cls.campo_persona_id = persona_id
        return cls

    @classmethod
    def clave(cls, clave):
        cls.campo_clave = clave
        return cls

    @classmethod
    def habilitado(cls, habilitado):
        cls.campo_habilitado = habilitado
        return cls

    @classmethod
    def construir(cls):
        return Usuario(
            id=cls.campo_id,
            persona_id=cls.campo_persona_id,
            clave=cls.campo_clave,
            habilitado=cls.campo_habilitado,
            usuario_id=cls.campo_usuario_id
        )
