class Pessoa:
    def __init__(
        self,
        nome,
        cpf,
        data_nascimento,
        fotografia,
        impressao_digital,
        data_emissao
    ):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.fotografia = fotografia
        self.impressao_digital = impressao_digital
        self.data_emissao = data_emissao

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")