class Renovacao:

    @staticmethod
    def renovar(banco, documento, nova_data):
        atualizado = banco.atualizar_data_emissao(documento, nova_data)
        if atualizado:
            print("Documento renovado com sucesso.")
        else:
            print("Documento não encontrado.")