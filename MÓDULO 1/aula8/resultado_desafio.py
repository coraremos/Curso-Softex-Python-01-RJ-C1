# Desafio de Programação: Validação de Triângulo
#ESTUDAR A FORMA DE FAZER COM TRY! 
# >try: / >except ValueError: / >>print("Erro: entrada inválida!")


while True:
    lA = input('Digite o tamanho do lado A: ')
    lB = input('Digite o tamanho do lado B: ')
    lC = input('Digite o tamanho do lado C: ')
    lados = [lA,lB,lC]
    for numero in lados:
        #teste se a entrada de dados é um número e se é positivo:
        if numero.isdigit():
            pass
        else:
            print(f'O dado {numero} é inválido, digite somente números inteiros e positivos.')
    
    lA = int(lA)
    lB = int(lB)
    lC = int(lC)

    for inteiros in lados:
        #aplicando as duas condições como verdade, 
        # usando o método abs() para o cálculo de diferenças resultar sempre em um núm absoluto:
        if (lB+lC) > lA and (lA+lC) > lB and (lA+lB) > lC and abs(lB-lC) < lA and abs(lA-lC) < lB and abs(lA-lB) < lC:
            print('é um triângulo!')
        #se as condições acima forem mentira:
        else:
            print('não é um triângulo...')

#ENUNCIADO

'''
Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número.
'''