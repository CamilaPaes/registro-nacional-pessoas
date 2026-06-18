class Relatorios:

    @staticmethod
    def listar(banco):
        registros = banco.listar_todos()
        print("\n===== REGISTROS =====")
        if not registros:
            print("Nenhum registro encontrado.")
        for pessoa in registros:
            print(pessoa)

    @staticmethod
    def quantidade_tramites(banco):
        contagem = banco.contar_por_tipo()
        identidade = contagem.get("DocumentoIdentidade", 0)
        residencia = contagem.get("AutorizacaoResidencia", 0)
        refugio = contagem.get("AutorizacaoRefugio", 0)
        total = identidade + residencia + refugio

        print("\n===== RELATÓRIO =====")
        print(f"Documentos de Identidade:   {identidade}")
        print(f"Autorizações de Residência: {residencia}")
        print(f"Autorizações de Refúgio:    {refugio}")
        print(f"Total:                      {total}")