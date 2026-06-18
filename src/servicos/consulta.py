class Consulta:

    @staticmethod
    def buscar_por_documento(banco, documento):
        return banco.buscar_por_documento(documento)

    @staticmethod
    def buscar_por_nome(banco, nome):
        return banco.buscar_por_nome(nome)

    @staticmethod
    def buscar_por_tipo(banco, tipo):
        return banco.buscar_por_tipo(tipo)