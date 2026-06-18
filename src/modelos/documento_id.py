from src.modelos.tramite import Tramite

class DocumentoIdentidade(Tramite):

    def __init__(self, nome, documento, foto, digital, data_emissao):
        super().__init__(
            nome,
            documento,
            foto,
            digital,
            data_emissao
        )

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Documento: {self.documento} | "
            f"Emissão: {self.data_emissao}"
        )