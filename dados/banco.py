import sqlite3
import json


class Banco:
    def __init__(self, caminho_db="sistema_registro.db"):
        self.__caminho = caminho_db
        self.__criar_tabelas()

    def __conectar(self):
        return sqlite3.connect(self.__caminho)

    def __criar_tabelas(self):
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tramites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    documento TEXT UNIQUE NOT NULL,
                    foto TEXT,
                    digital TEXT,
                    data_emissao TEXT,
                    extras TEXT
                )
            """)
            con.commit()

    # ------------------------------------------------------------------ #
    #  Métodos usados pelos serviços                                       #
    # ------------------------------------------------------------------ #

    def inserir(self, tramite):
        """Persiste um trâmite no banco."""
        tipo = tramite.__class__.__name__
        extras = self.__extras_para_dict(tramite, tipo)

        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO tramites (tipo, nome, documento, foto, digital, data_emissao, extras)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                tipo,
                tramite.nome,
                tramite.documento,
                tramite.foto,
                tramite.digital,
                tramite.data_emissao,
                json.dumps(extras)
            ))
            con.commit()

    def buscar_por_documento(self, documento):
        """Retorna o objeto trâmite correspondente ao documento, ou None."""
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM tramites WHERE documento = ?", (documento,))
            row = cur.fetchone()
        return self.__row_para_objeto(row) if row else None

    def buscar_por_nome(self, nome):
        """Retorna lista de trâmites cujo nome contenha o texto buscado."""
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM tramites WHERE nome LIKE ?", (f"%{nome}%",))
            rows = cur.fetchall()
        return [self.__row_para_objeto(r) for r in rows]

    def buscar_por_tipo(self, tipo):
        """Retorna lista de trâmites do tipo informado."""
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM tramites WHERE tipo = ?", (tipo,))
            rows = cur.fetchall()
        return [self.__row_para_objeto(r) for r in rows]

    def listar_todos(self):
        """Retorna todos os trâmites cadastrados."""
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM tramites")
            rows = cur.fetchall()
        return [self.__row_para_objeto(r) for r in rows]

    def atualizar_data_emissao(self, documento, nova_data):
        """Atualiza a data de emissão de um trâmite (renovação)."""
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute(
                "UPDATE tramites SET data_emissao = ? WHERE documento = ?",
                (nova_data, documento)
            )
            con.commit()
        return cur.rowcount > 0

    def remover(self, documento):
        """Remove um trâmite pelo número do documento (revogação)."""
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("DELETE FROM tramites WHERE documento = ?", (documento,))
            con.commit()
        return cur.rowcount > 0

    def contar_por_tipo(self):
        """Retorna um dicionário {tipo: quantidade}."""
        with self.__conectar() as con:
            cur = con.cursor()
            cur.execute("SELECT tipo, COUNT(*) FROM tramites GROUP BY tipo")
            rows = cur.fetchall()
        return {tipo: qtd for tipo, qtd in rows}

    # ------------------------------------------------------------------ #
    #  Helpers internos                                                    #
    # ------------------------------------------------------------------ #

    @staticmethod
    def __extras_para_dict(tramite, tipo):
        extras = {}
        if tipo == "AutorizacaoResidencia":
            extras["pais_origem"] = tramite.pais_origem
            extras["data_vencimento"] = tramite.data_vencimento
        elif tipo == "AutorizacaoRefugio":
            extras["pais_origem"] = tramite.pais_origem
            extras["motivo_refugio"] = tramite.motivo_refugio
        return extras

    @staticmethod
    def __row_para_objeto(row):
        """Converte uma linha do banco num objeto do modelo correto."""
        from src.modelos.documento_id import DocumentoIdentidade
        from src.modelos.autorizacao_residencia import AutorizacaoResidencia
        from src.modelos.autorizacao_refugio import AutorizacaoRefugio

        # row: (id, tipo, nome, documento, foto, digital, data_emissao, extras)
        _, tipo, nome, documento, foto, digital, data_emissao, extras_json = row
        extras = json.loads(extras_json) if extras_json else {}

        if tipo == "DocumentoIdentidade":
            return DocumentoIdentidade(nome, documento, foto, digital, data_emissao)

        if tipo == "AutorizacaoResidencia":
            return AutorizacaoResidencia(
                nome, documento, foto, digital, data_emissao,
                extras.get("pais_origem", ""),
                extras.get("data_vencimento", "")
            )

        if tipo == "AutorizacaoRefugio":
            return AutorizacaoRefugio(
                nome, documento, foto, digital, data_emissao,
                extras.get("pais_origem", ""),
                extras.get("motivo_refugio", "")
            )

        return None