from app import ma


class EsquemaComandoRespuesta(ma.Schema):
    class Meta:
        fields = ('valor',)
