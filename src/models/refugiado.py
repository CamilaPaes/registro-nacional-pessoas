from .pessoa import Pessoa


class Refugiado(Pessoa):
    def __init__(
        self,
        nome,
        cpf,
        data_nascimento,
        fotografia,
        impressao_digital,
        data_emissao,
        pais_origem,
        motivo_refugio
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
        self.motivo_refugio = motivo_refugio

    def tipo_documento(self):
        return "Documento de Refúgio"