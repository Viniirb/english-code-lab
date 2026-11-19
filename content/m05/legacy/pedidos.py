# Calcula o total de um pedido
def calcular_total(itens, desconto=0):
    """Soma o preço dos itens e aplica o desconto."""
    total = 0
    for item in itens:
        total += item["preco"] * item["quantidade"]
    return aplicar_desconto(total, desconto)


def aplicar_desconto(valor, percentual):
    # percentual vai de 0 a 100
    if percentual < 0 or percentual > 100:
        raise ValueError("percentual inválido")
    return valor - valor * percentual / 100


def itens_caros(itens, limite):
    # retorna os itens com preço acima do limite
    return [item for item in itens if item["preco"] > limite]


class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, " + self.nome
