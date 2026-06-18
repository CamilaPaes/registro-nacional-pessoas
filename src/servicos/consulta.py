class Consulta:

    @staticmethod
    def buscar_por_documento(banco, documento):

        for pessoa in banco.registros:

            if pessoa.documento == documento:
                return pessoa

        return None

    @staticmethod
    def buscar_por_nome(banco, nome):

        resultado = []

        for pessoa in banco.registros:

            if nome.lower() in pessoa.nome.lower():
                resultado.append(pessoa)

        return resultado

    @staticmethod
    def buscar_por_tipo(banco, tipo):

        resultado = []

        for pessoa in banco.registros:

            if pessoa.__class__.__name__.lower() == tipo.lower():

                resultado.append(pessoa)

        return resultado