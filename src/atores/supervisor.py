from atores.pessoa import Pessoa


class Supervisor(Pessoa):
    def __init__(self, nome, cpf, setor):
        super().__init__(nome, cpf)
        self.__setor = setor

    @property
    def setor(self):
        return self.__setor

    def aprovar_tramite(self, tramite):
        print(f"Supervisor {self.nome} aprovou {tramite}")

    def gerar_relatorio(self):
        print("Relatório gerado com sucesso.")