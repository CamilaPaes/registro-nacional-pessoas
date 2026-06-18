class Cadastro:
 
    @staticmethod
    def cadastrar(banco, tramite):
        try:
            banco.inserir(tramite)
            print("\n✔ Cadastro realizado com sucesso!\n")
        except Exception as e:
            # O erro mais comum é documento duplicado (UNIQUE constraint)
            if "UNIQUE" in str(e):
                print("Erro: já existe um registro com esse número de documento.")
            else:
                print(f"Erro ao cadastrar: {e}")
 