def pegar_taxa_desconto(valor_inicial):
    return 0.10 * valor_inicial 

def calcular_taxa_desconto(preco: float):
    taxa_desconto = pegar_taxa_desconto(0.9)
    return preco - (preco * taxa_desconto)



