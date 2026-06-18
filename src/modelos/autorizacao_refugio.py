from src.modelos.tramite import Tramite

class AutorizacaoRefugio(Tramite):

    def __init__(
        self,
        nome,
        documento,
        foto,
        digital,
        data_emissao,
        pais_origem,
        motivo_refugio
    ):
        super().__init__(nome, documento, foto, digital, data_emissao)

        self.__pais_origem = pais_origem
        self.__motivo_refugio = motivo_refugio

    @property
    def pais_origem(self):
        return self.__pais_origem

    @property
    def motivo_refugio(self):
        return self.__motivo_refugio

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Documento: {self.documento} | "
            f"País: {self.pais_origem} | "
            f"Motivo: {self.motivo_refugio}"
        )