class Relatorios:

    @staticmethod
    def quantidade_tramites(banco):

        identidade = 0
        residencia = 0
        refugio = 0

        for item in banco.registros:

            if item.__class__.__name__ == "DocumentoIdentidade":
                identidade += 1

            elif item.__class__.__name__ == "AutorizacaoResidencia":
                residencia += 1

            elif item.__class__.__name__ == "AutorizacaoRefugio":
                refugio += 1

        print("\n===== RELATÓRIO =====")
        print(f"Documentos de Identidade: {identidade}")
        print(f"Autorizações de Residência: {residencia}")
        print(f"Autorizações de Refúgio: {refugio}")
        print(f"Total: {len(banco.registros)}")

    @staticmethod
    def listar(banco):

        print("\n===== REGISTROS =====")

        for pessoa in banco.registros:
            print(pessoa)