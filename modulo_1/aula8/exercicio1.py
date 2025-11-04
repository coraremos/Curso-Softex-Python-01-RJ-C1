'''Engenharia de software: 
"O projeto" (requisitos)
    requisitos funcionais - 
    o que precisa ter? (UX - o que o usuário irá realizar ex.: permitir login, permitir mostrar dados)
    
    requisitos não-funcionais - 
    como precisa ser? (o que funciona apesar da vontade do USER; ex.: site responsivo)

PRINCIPIOS SOLID: cinco regras que guiam a crição do seu código
S - single responsibility (organizar cada passo em uma linha)
O - open/closed (bloco de logica que funciona mesmo se retirar os blocos 'de baixo')
L - liskov substitution (caso substitua os dados não comprometer no funcionamento total)
I - interface segregation (evitar repetir codigo para não pesar no total)
D - dependency inversion (deixar o codigo claro para que outras pessoas entendam)

código limpo; nomes claros; funções pequenas (funções além das nativas py); 
não se repita - principio DRY 'dont repeat yourself'. 
'''

#exercicio2: Validação e formatação de telefone

#3 ou mais digitos iguais
# se for válido, formatá-lo para (XX)XXXXX-XXXX


while True:
    formato = '(XX)XXXXX-XXXX'
    telefone = input('insira aqui seu número de telefone: ')
    if not telefone.isdigit():
        print('você digitou errado, tente novamente:')
    else:
        print('você digitou corretamente')
        if len(telefone) != 11:
            print('porém não há caracteres suficientes')
        else: 
            numero_formatado = formato.replace('X', telefone)
            print(numero_formatado)


contador = 0

for numero in telefone:
    if numero in digitos:
        contador += 1

else:
    valido = True
    for c in numeros:
        cont = 0
        for d in numeros:
            if d == c:
                cont += 1
            if cont >= 3:
                valido = False
                break
        

