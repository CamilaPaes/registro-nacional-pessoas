from .pessoa import Pessoa


class Estrangeiro(Pessoa):
    def __init__(
        self,
        nome,
        cpf,
        data_nascimento,
        fotografia,
        impressao_digital,
        data_emissao,
        pais_origem,
        data_validade
    ):
        super().__init__(
            nome,
            cpf,
            data_nascimento,
            fotografia,
            impressao_digital,
            data_emissao
        )

        self.pais_origem = pais_origem
        self.data_validade = data_validade

    def tipo_documento(self):
        return "Permissão de Residência"