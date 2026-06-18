class Revogacao:

    @staticmethod
    def revogar(banco, documento):

        for pessoa in banco.registros:

            if pessoa.documento == documento:

                banco.registros.remove(pessoa)

                print("Documento revogado.")

                return

        print("Documento não encontrado.")