'''
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:
'''

while True:
    lA = input('Digite o tamanho do lado A: ')
    lB = input('Digite o tamanho do lado B: ')
    lC = input('Digite o tamanho do lado C: ')
    lados = [lA,lB,lC]
    for numero in lados:
        if numero.isdigit():
            pass
        else:
            print(f'O dado {numero} é inválido, digite somente números inteiros e positivos.')
    
    lA = int(lA)
    lB = int(lB)
    lC = int(lC)

    for inteiros in lados:
                if (lB+lC) < lA:
                    print('ok')
                elif (lA+lC) < lB:
                    print('ok')
                elif (lA+lB) < lC:
                    print('ok')
                elif (lB-lC) > lA:
                    print('ok')
                elif (lA-lC) > lB:
                    print('ok')
                elif (lA-lB) > lC:
                    print('ok')
                else:
                    print('não é um triângulo!!!')


'''

'''