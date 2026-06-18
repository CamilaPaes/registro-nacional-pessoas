from src.modelos.tramite import Tramite

class AutorizacaoResidencia(Tramite):

    def __init__(
        self,
        nome,
        documento,
        foto,
        digital,
        data_emissao,
        pais_origem,
        data_vencimento
    ):

        super().__init__(
            nome,
            documento,
            foto,
            digital,
            data_emissao
        )

        self.__pais_origem = pais_origem
        self.__data_vencimento = data_vencimento

    @property
    def pais_origem(self):
        return self.__pais_origem

    @property
    def data_vencimento(self):
        return self.__data_vencimento