
class Tramite:
    def __init__(self, nome, documento, foto, digital, data_emissao):
        self.__nome = nome
        self.__documento = documento
        self.__foto = foto
        self.__digital = digital
        self.__data_emissao = data_emissao

    @property
    def nome(self):
        return self.__nome

    @property
    def documento(self):
        return self.__documento

    @property
    def foto(self):
        return self.__foto

    @property
    def digital(self):
        return self.__digital

    @property
    def data_emissao(self):
        return self.__data_emissao

    def __str__(self):
        return f"{self.__nome} - Documento: {self.__documento}"