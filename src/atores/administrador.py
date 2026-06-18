from atores.pessoa import Pessoa


class Administrador(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def cadastrar_usuario(self, usuario):
        print(f"Usuário {usuario.nome} cadastrado.")

    def remover_usuario(self, usuario):
        print(f"Usuário {usuario.nome} removido.")