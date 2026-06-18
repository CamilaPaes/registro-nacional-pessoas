from atores.pessoa import Pessoa


class Solicitante(Pessoa):
    def __init__(self, nome, cpf, tipo):
        super().__init__(nome, cpf)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    def solicitar_documento(self):
        print(f"{self.nome} realizou uma solicitação.")

    def consultar_processo(self):
        print(f"{self.nome} consultou o andamento do processo.")