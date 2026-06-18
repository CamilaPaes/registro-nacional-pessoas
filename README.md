# Sistema de Registro Nacional de Pessoas

Projeto semestral — Centro Universitário Tiradentes de Pernambuco  
Engenharia de Software · Prof. Dr. David Barrientos · Semestre 2026.1

Sistema de linha de comando desenvolvido em Python para centralizar o registro de pessoas, contemplando três tipos de trâmites: emissão de documentos de identidade, autorização de residência para estrangeiros e autorização de refúgio.

---

## Funcionalidades

- Cadastro de trâmites por tipo (identidade, residência, refúgio)
- Busca por número de documento, nome ou tipo de trâmite
- Renovação e revogação de documentos
- Relatórios com listagem geral e contagem por categoria
- Controle de acesso baseado em perfis (Administrador, Supervisor, Funcionário de Registro, Solicitante)
- Persistência de dados com SQLite3 (arquivo local `sistema_registro.db`)

---

## Estrutura do projeto

```
projeto/
│
├── main.py                        # Ponto de entrada da aplicação
│
├── dados/
│   └── banco.py                   # Classe Banco — conexão e operações SQLite3
│
└── src/
    ├── atores/
    │   ├── pessoa.py
    │   ├── administrador.py
    │   ├── supervisor.py
    │   ├── funcionario_registro.py
    │   └── solicitante.py
    │
    ├── modelos/
    │   ├── tramite.py             # Classe base com atributos comuns
    │   ├── documento_id.py
    │   ├── autorizacao_residencia.py
    │   └── autorizacao_refugio.py
    │
    └── servicos/
        ├── cadastro.py
        ├── consulta.py
        ├── renovacao.py
        ├── revogacao.py
        └── relatorios.py
```

---

## Requisitos

- Python 3.8 ou superior
- Sem dependências externas — SQLite3 já está incluso na biblioteca padrão do Python

---

## Como executar

Clone o repositório e execute o arquivo principal:

```bash
python main.py
```

Na inicialização, o sistema solicita o perfil de acesso:

```
=================================
LOGIN
=================================
1 - Administrador
2 - Supervisor
3 - Funcionário de Registro
4 - Solicitante
```

O banco de dados `sistema_registro.db` é criado automaticamente na primeira execução, na mesma pasta do projeto.

---

## Menu principal

```
===================================
 SISTEMA DE REGISTRO NACIONAL
===================================
1 - Documento de Identidade
2 - Autorização de Residência
3 - Autorização de Refúgio
4 - Buscar por Documento
5 - Buscar por Nome
6 - Buscar por Tipo
7 - Renovar Documento
8 - Revogar Documento
9 - Relatórios
0 - Sair
```

---

## Tipos de trâmite

### Documento de Identidade
Campos: nome, número do documento, foto, impressão digital, data de emissão.

### Autorização de Residência
Campos: nome, número do documento, foto, impressão digital, data de emissão, país de origem, data de vencimento.

### Autorização de Refúgio
Campos: nome, número do documento, foto, impressão digital, data de emissão, país de origem, motivo do refúgio.

---

## Banco de dados

Os dados são persistidos localmente em um arquivo SQLite3 (`sistema_registro.db`) com a seguinte estrutura:

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER | Chave primária, gerada automaticamente |
| `tipo` | TEXT | Classe do trâmite (`DocumentoIdentidade`, etc.) |
| `nome` | TEXT | Nome do solicitante |
| `documento` | TEXT | Número do documento (único) |
| `foto` | TEXT | Referência à foto |
| `digital` | TEXT | Referência à impressão digital |
| `data_emissao` | TEXT | Data de emissão do documento |
| `extras` | TEXT | Campos específicos por tipo, armazenados em JSON |

---

## Perfis de acesso

| Perfil | Descrição |
|---|---|
| Administrador | Gerencia usuários do sistema |
| Supervisor | Aprova trâmites e gera relatórios |
| Funcionário de Registro | Cadastra e atualiza pessoas |
| Solicitante | Realiza solicitações e acompanha processos |

---

## Decisões de projeto

**Herança:** `DocumentoIdentidade`, `AutorizacaoResidencia` e `AutorizacaoRefugio` herdam de `Tramite`, que centraliza os atributos comuns e o método `__str__`.

**Serviços estáticos:** as classes de serviço (`Cadastro`, `Consulta`, `Renovacao`, `Revogacao`, `Relatorios`) utilizam apenas métodos estáticos, funcionando como camadas de operação sem estado próprio.

**Persistência desacoplada:** toda a lógica de banco de dados está concentrada em `dados/banco.py`. Os modelos e serviços não conhecem SQL — conversam apenas com a interface pública da classe `Banco`.

**Campos extras em JSON:** atributos específicos de cada tipo de trâmite (como `pais_origem`, `data_vencimento` e `motivo_refugio`) são serializados em JSON na coluna `extras`, evitando a necessidade de tabelas separadas e mantendo o esquema simples.

---

## Autores

Projeto desenvolvido como atividade avaliativa da disciplina de Engenharia de Software.