from loja import Loja
from produto_eletronico import ProdutoEletronico
from produto import Produto

loja = Loja()

produto1 = Produto("Caneta", 2.0, 25)
produto2 = Produto("Lápis", 1.5, 50)

loja.adicionar_produto_ao_estoque(produto1, 20)
loja.adicionar_produto_ao_estoque(produto2, 30)

print(f"Estoque de {produto1.nome}: {loja.verificar_estoque_de_produto('Caneta')}")
print(f"Estoque de {produto2.nome}: {loja.verificar_estoque_de_produto('Lápis')}")

produto1.set_quantidade_em_estoque(25)
loja.estoque[produto1.nome] = 25

print('Atualização de estoque:')
print(f"Estoque de {produto1.nome}: {loja.verificar_estoque_de_produto('Caneta')}")
print(f"Estoque de {produto2.nome}: {loja.verificar_estoque_de_produto('Lápis')}")