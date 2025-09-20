from pessoa import Pessoa

pessoa_1 = Pessoa("João", 18)
pessoa_2 = Pessoa("Maria", 17)

print("Registro de nascimento:")
print(f"Nome: {pessoa_1.nome}.") 
print(f"Idade: {pessoa_1.idade} anos.") 
print(f"Nome: {pessoa_2.nome}.") 
print(f"Idade: {pessoa_2.idade} anos.") 

pessoa_1.comer('maçã')
pessoa_1.comer('maçã')
pessoa_1.parar_comer()
pessoa_1.parar_comer()
pessoa_1.comer('uvas')

pessoa_1.falar('Oi!')
pessoa_1.parar_comer()
pessoa_1.falar('Oi!')

pessoa_1.comer('biscoito')
pessoa_1.parar_falar()
pessoa_1.comer('biscoito')