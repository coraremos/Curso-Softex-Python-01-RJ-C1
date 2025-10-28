'''Maior Sequência Contígua

Crie uma função que receba uma lista de números e
retorne a soma máxima de qualquer sublista contígua
(algoritmo de Kadane - Avançado).

função, for, if/else, max(), print
'''

def kadane(lista):
    # trata caso de lista vazia
    if not lista:
        return None  # ou 0, conforme especificação
    
    # índices iniciais
    max_terminando = max_ate_agora = lista[0]
    inicio = fim = temp_inicio = 0


    for i in range(1, len(lista)):
        if lista[i] > max_terminando + lista[i]:
            max_terminando = lista[i] 
            #encontra o valor acima e vai substituindo até achar o valor máximo
            temp_inicio = i
        else:
            max_terminando += lista[i]
        if max_terminando > max_ate_agora:
            max_ate_agora = max_terminando
            inicio, fim = temp_inicio, i
    return max_ate_agora, inicio, fim

# exemplos
print(kadane([ -2, 1, -3, 4, -1, 2, 1, -5, 4]))  # esperado: (6, 3, 6) -> subarray [4,-1,2,1]
print(kadane([1,2,3,4]))                         # esperado: (10, 0, 3)
print(kadane([-5, -2, -3]))                      # esperado: (-2, 1, 1) (maior elemento)
print(kadane([]))                                # esperado: None