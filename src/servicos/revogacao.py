class Revogacao:

    @staticmethod
    def revogar(banco, documento):
        removido = banco.remover(documento)
        if removido:
            print("Documento revogado com sucesso.")
        else:
            print("Documento não encontrado.")