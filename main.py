from dados.banco import Banco

from src.modelos.documento_id import DocumentoIdentidade
from src.modelos.autorizacao_residencia import AutorizacaoResidencia
from src.modelos.autorizacao_refugio import AutorizacaoRefugio

from src.servicos.cadastro import Cadastro
from src.servicos.consulta import Consulta
from src.servicos.revogacao import Revogacao
from src.servicos.renovacao import Renovacao
from src.servicos.relatorios import Relatorios


print("=================================")
print("LOGIN")
print("=================================")
print("1 - Administrador")
print("2 - Supervisor")
print("3 - Funcionário de Registro")
print("4 - Solicitante")

perfil = input("Escolha o perfil: ")

print("\nAcesso concedido.\n")

banco = Banco()

while True:

    print("\n===================================")
    print(" SISTEMA DE REGISTRO NACIONAL")
    print("===================================")
    print("1 - Documento de Identidade")
    print("2 - Autorização de Residência")
    print("3 - Autorização de Refúgio")
    print("4 - Buscar por Documento")
    print("5 - Buscar por Nome")
    print("6 - Buscar por Tipo")
    print("7 - Renovar Documento")
    print("8 - Revogar Documento")
    print("9 - Relatórios")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":

        nome = input("Nome: ")
        documento = input("Documento: ")
        foto = input("Foto: ")
        digital = input("Digital: ")
        data = input("Data emissão: ")

        obj = DocumentoIdentidade(
            nome,
            documento,
            foto,
            digital,
            data
        )

        Cadastro.cadastrar(banco, obj)

    elif opcao == "2":

        nome = input("Nome: ")
        documento = input("Documento: ")
        foto = input("Foto: ")
        digital = input("Digital: ")
        data = input("Data emissão: ")
        pais = input("País de origem: ")
        vencimento = input("Data de vencimento: ")

        obj = AutorizacaoResidencia(
            nome,
            documento,
            foto,
            digital,
            data,
            pais,
            vencimento
        )

        Cadastro.cadastrar(banco, obj)

    elif opcao == "3":

        nome = input("Nome: ")
        documento = input("Documento: ")
        foto = input("Foto: ")
        digital = input("Digital: ")
        data = input("Data emissão: ")
        pais = input("País de origem: ")
        motivo = input("Motivo do refúgio: ")

        obj = AutorizacaoRefugio(
            nome,
            documento,
            foto,
            digital,
            data,
            pais,
            motivo
        )

        Cadastro.cadastrar(banco, obj)

    elif opcao == "4":

        doc = input("Documento: ")

        pessoa = Consulta.buscar_por_documento(
            banco,
            doc
        )

        print(pessoa if pessoa else "Não encontrado.")

    elif opcao == "5":

        nome = input("Nome: ")

        resultado = Consulta.buscar_por_nome(
            banco,
            nome
        )

        for item in resultado:
            print(item)

    elif opcao == "6":

        print("DocumentoIdentidade")
        print("AutorizacaoResidencia")
        print("AutorizacaoRefugio")

        tipo = input("Tipo: ")

        resultado = Consulta.buscar_por_tipo(
            banco,
            tipo
        )

        for item in resultado:
            print(item)

    elif opcao == "7":

        doc = input("Documento: ")

        pessoa = Consulta.buscar_por_documento(
            banco,
            doc
        )

        if pessoa:

            nova = input("Nova data de emissão: ")

            Renovacao.renovar(
                pessoa,
                nova
            )

        else:

            print("Documento não encontrado.")

    elif opcao == "8":

        doc = input("Documento: ")

        Revogacao.revogar(
            banco,
            doc
        )

    elif opcao == "9":

        Relatorios.listar(banco)

        Relatorios.quantidade_tramites(
            banco
        )

    elif opcao == "0":

        print("Sistema encerrado.")

        break

    else:

        print("Opção inválida.")