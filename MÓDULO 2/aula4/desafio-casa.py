''' EXERCICIO 1

Crie um programa que recebe uma frase do usuário e faz uma análise completa sobre ela,
mostrando:
● A quantidade de palavras na frase.
● A quantidade de vogais (a, e, i, o, u).
● A quantidade de consoantes.
● Se a frase é um palíndromo (ou seja, se ela pode ser lida da mesma forma de trás para
frente, ignorando espaços e letras maiúsculas).
Exemplo de Execução:
Digite uma frase para analisar: A sacada da casa
--- Resumo da Análise ---
Palavras: 4
Vogais: 6
Consoantes: 6
É um palíndromo? Sim
'''

frase = input('Digite aqui uma frase: ').lower().replace("-","").replace(",","").replace(".","")

def quant_palavras(frase:str) -> int:
    return len(frase.split())

def quant_vogais(frase:str) -> int:
     lista_vogais = 'aeiouáéíóú'
     return sum(1 for letra in frase if letra in lista_vogais)

def quant_consoantes(frase:str) -> int:
     lista_consoantes = 'bcdfghjklmnpqrstvxwzñç'
     return sum(1 for letra in frase if letra in lista_consoantes)
     
def result_palindromo(frase: str) -> str:
    frase_inicial = frase.replace(" ","")
    return 'Sim' if frase_inicial == frase_inicial[::-1] else 'Não'

palavras = quant_palavras(frase)
vogais = quant_vogais(frase)
consoantes = quant_consoantes(frase)
resposta = result_palindromo(frase)

print(f'Palavras: {palavras}.')
print(f'Vogais: {vogais}.')
print(f'Consoantes: {consoantes}.')  
print(f'É um polímetro: {resposta}')   