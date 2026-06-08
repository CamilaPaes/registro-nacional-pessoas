from .pessoa import Pessoa


class Cidadao(Pessoa):
    def __init__(
        self,
        nome,
        cpf,
        data_nascimento,
        fotografia,
        impressao_digital,
        data_emissao,
        numero_documento
    ):
        super().__init__(
            nome,
            cpf,
            data_nascimento,
            fotografia,
            impressao_digital,
            data_emissao
        )

        self.numero_documento = numero_documento