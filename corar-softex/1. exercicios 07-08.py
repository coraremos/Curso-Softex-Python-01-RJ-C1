'''Módulo 1: Variáveis, Operadores e if Simples

Exercício 1: Verificador de Positivo
● Peça ao usuário para digitar um número inteiro.
● Use uma estrutura if simples para verificar se o número é maior que zero.
● Se for, imprima "O número é positivo!".

Exercício 2: Calculadora de Desconto
● Peça ao usuário para digitar o preço original de um produto (float).
● Se o preço for maior que R$ 100,00, aplique um desconto de 10% e imprima o novo preço.
● Use o operador de multiplicação (*) e subtração (-).

Exercício 3: Verificador de Divisibilidade
● Peça ao usuário um número inteiro.
● Verifique se o número é divisível por 5 (use o operador %).
● Se for, imprima "O número é divisível por 5".

    Módulo 2: if-else e Lógica Relacional

Exercício 4: Verificador de Senha
● Defina uma senha secreta em uma variável (str, por exemplo, "python123").
● Peça ao usuário para digitar uma senha.
● Use if-else para verificar se a senha digitada é igual à senha secreta. Imprima "Acesso concedido" ou "Senha incorreta".

Exercício 5: Maior de Dois Números
● Peça ao usuário para digitar dois números inteiros.
● Use if-else para descobrir qual dos dois é o maior e imprima o resultado.

Exercício 6: Verificador de Par ou Ímpar
● Peça ao usuário um número inteiro.
● Use o operador de módulo (%) e uma estrutura if-else para determinar e imprimir se o número é "par" ou "ímpar".

Módulo 3: if-elif-else para Múltiplas Condições

Exercício 7: Classificador de Idade
● Peça a idade de uma pessoa.
● Use if-elif-else para classificar a idade em:
○ "Criança" (0 a 12 anos)
○ "Adolescente" (13 a 17 anos)
○ "Adulto" (18 a 59 anos)
○ "Idoso" (60 anos ou mais)

Exercício 8: Avaliador de Notas
● Peça a nota de um aluno (float).
● Use if-elif-else para atribuir um conceito:
○ = 9.0: Conceito A
○ = 7.0: Conceito B
○ = 5.0: Conceito C
○ < 5.0: Conceito D

Exercício 9: Categoria de CNH
● Peça a idade e se o usuário tem CNH (True ou False).
● Use if-elif-else com operadores lógicos (and e or) para:
○ Se for maior de 18 e tiver CNH: "Pode dirigir."
○ Se for maior de 18 e não tiver CNH: "Precisa tirar a CNH."
○ Se for menor de 18: "Não pode dirigir."

    Módulo 4: Repetição com while Simples

Exercício 10: Contador Regressivo
● Peça um número inteiro ao usuário.
● Use um while para fazer uma contagem regressiva a partir desse número até 0. Imprima cada número.

Exercício 11: Tabuada Simples
● Peça um número ao usuário.
● Use um while para imprimir a tabuada desse número, de 1 a 10.
○ Exemplo: 5 x 1 = 5, 5 x 2 = 10, etc.

Exercício 12: Acumulador de Soma
● Peça ao usuário para digitar 5 números.
● Use um while com um contador para somar todos os números digitados e imprimir o resultado final.
Módulo 5: while com break e Validação de Dados

Exercício 13: Login com Tentativas
● Defina uma senha secreta.
● Use um while True e um contador de tentativas (máximo de 3).
● Se o usuário acertar a senha, imprima "Login bem-sucedido!" e use break.
● Se o usuário errar 3 vezes, imprima "Tentativas esgotadas!" e pare o programa.

Exercício 14: Somador de Números Positivos
● Use um while True para pedir números ao usuário.
● Some todos os números positivos.
● Se o usuário digitar um número negativo, use break para sair do loop e imprima a soma
total.

Exercício 15: Validação de E-mail
● Use um while True para pedir um e-mail ao usuário.
● Verifique se o e-mail contém o caractere @.
● Se contiver, imprima "E-mail válido" e use break.
● Se não contiver, imprima "E-mail inválido. Digite novamente."

    Módulo 6: Desafios Combinados e Lógica Avançada

Exercício 16: Jogo de Adivinhação com Dicas
● Defina um número secreto.
● Use um while True e um contador de tentativas.
● A cada tentativa, diga se o palpite é "maior" ou "menor" que o número secreto.
● Quando o usuário acertar, imprima a mensagem de vitória e quantas tentativas foram necessárias.

Exercício 17: Sequência de Fibonacci
● Peça um número n ao usuário.
● Use um while para gerar e imprimir os primeiros n termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, ...).

Exercício 18: Calculadora de Fatorial
● Peça um número n ao usuário.
● Use um while para calcular o fatorial de n (por exemplo, 5! = 5 * 4 * 3 * 2 * 1).
● Imprima o resultado.

Exercício 19: Caixa Eletrônico Simplificado
● Defina um saldo inicial.
● Use um while True para apresentar um menu ao usuário:
○
1. Sacar
○
2. Depositar
○
3. Ver saldo
○
4. Sair
● Use if-elif-else para processar a escolha do usuário.
○ Se sacar, verifique se há saldo suficiente.
○ Se depositar, adicione o valor ao saldo.
○ Se sair, use break.
● Valide as entradas do usuário (por exemplo, não permitir saque de valor negativo).
Exercício 20: Jogo da Forca Simplificado
● Defina uma palavra secreta em uma variável (str).
● Use um while para dar ao usuário 5 chances de adivinhar a palavra.
● A cada tentativa, o usuário digita uma letra.
● Se a letra estiver na palavra, exiba as letras já descobertas (ex: _ y t _ _ n).
● Se a letra não estiver, diminua as chances.
● Se o usuário acertar todas as letras, imprima a palavra completa e uma mensagem de vitória. Se as chances acabarem, imprima a palavra e uma mensagem de derrota.

'''