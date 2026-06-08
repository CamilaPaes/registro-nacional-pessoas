from models.cidadao import Cidadao

cidadao = Cidadao(
    "Maria Silva",
    "12345678900",
    "01/01/1990",
    "foto.jpg",
    "digital",
    "01/01/2025",
    "RG123456"
)

print(cidadao.tipo_documento())
cidadao.exibir_dados()