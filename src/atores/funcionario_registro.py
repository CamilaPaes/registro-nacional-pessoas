from atores.pessoa import Pessoa


class FuncionarioRegistro(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    def cadastrar_pessoa(self, pessoa):
        print(f"{self.nome} cadastrou {pessoa.nome}")

    def atualizar_pessoa(self, pessoa):
        print(f"{self.nome} atualizou os dados de {pessoa.nome}")