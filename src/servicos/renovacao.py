class Renovacao:

    @staticmethod
    def renovar(tramite, nova_data):

        tramite._Tramite__data_emissao = nova_data

        print("Documento renovado.")