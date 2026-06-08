from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(
        self,
        nome,
        cpf,
        data_nascimento,
        fotografia,
        impressao_digital,
        data_emissao
    ):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._fotografia = fotografia
        self._impressao_digital = impressao_digital
        self._data_emissao = data_emissao

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @abstractmethod
    def tipo_documento(self):
        pass

    def exibir_dados(self):
        print(f"Nome: {self._nome}")
        print(f"CPF: {self._cpf}")