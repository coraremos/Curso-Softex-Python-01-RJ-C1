#exercicio3: codificador e decodificador de frases

'''
frase = input('digite uma frase: ')
frase2 = frase.replace('a', '1').replace('e', '2').replace('i', '3').replace('o', '4').replace('u', '5')
frase3 = frase2.replace('1','a').replace('2','e').replace('3', 'i').replace('4', 'o').replace('5', 'u')
print(frase2)
print(frase3)
'''

# se a vogal(nova variável) estiver na frase, se a vogal for igual a 'a':
# pegue a frase e a substitua por uma nova frase onde será substituido 'a' por '1'.


frase_original = input('digite uma frase: ').lower()
frase_codificada = ''
frase_decodificada = ''

for vogal in frase_original:
    if vogal == 'a':
        frase_codificada = frase_original.replace('a', '1')
    elif vogal == 'e':
        frase_codificada = frase_original.replace('e', '2')
    elif vogal == 'i':
        frase_codificada = frase_original.replace('i', '3')
    elif vogal == 'o':
        frase_codificada = frase_original.replace('o', '4')
    elif vogal == 'u':
        frase_codificada = frase_original.replace('u', '5')
print(frase_codificada)
for numero in frase_codificada:
    if numero == '1':
        frase_decodificada = frase_codificada.replace('1', 'a')
    elif numero == '2':
        frase_decodificada = frase_codificada.replace('2', 'e')
    elif numero == '3':
        frase_decodificada = frase_codificada.replace('3', 'i')
    elif numero == '4':
        frase_decodificada = frase_codificada.replace('4', 'o')
    elif numero == '5':
        frase_decodificada = frase_codificada.replace('5', 'u')
print(frase_decodificada)

