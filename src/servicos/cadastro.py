class Cadastro:

    @staticmethod
    def cadastrar(banco, tramite):
        banco.registros.append(tramite)
        print("Cadastro realizado com sucesso.")