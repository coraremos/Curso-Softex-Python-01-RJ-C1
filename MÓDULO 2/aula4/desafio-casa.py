'''
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

vogais = 0
consoantes = 0
vogal = 'aeiouáéíóú'
consoante = 'bcdfghjklmnpqrstvxwzñç'

frase = input('Digite aqui uma frase: ').lower().replace("-","").replace(",","").replace(".","")

palavras = ""

for palavra in frase:
    palavras = len(frase.split())

frase = frase.replace(" ","")
indice = len(frase) - 1
frase_invertida = ''
for letra in frase:
        if letra in vogal:
            vogais += 1
        if letra in consoante:
            consoantes += 1
        if indice >= 0:
            frase_invertida += frase[indice]
            indice -= 1
            if frase == frase_invertida:
                resposta = 'Sim'
            else:
                resposta = 'Não'

print(f'Palavras: {palavras}.')
print(f'Vogais: {vogais}.')
print(f'Consoantes: {consoantes}.')  
print(f'É um polímetro: {resposta}')   




