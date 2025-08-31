# Desafio de Programação: Validação de Triângulo

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
        if (lB+lC) > lA or (lA+lC) > lB or (lA+lB) > lC or abs(lB-lC) < lA or abs(lA-lC) < lB or abs(lA-lB) < lC:
            print('é um triângulo!')
        #se as condições acima forem mentira:
        else:
            print('não é um triângulo...')

