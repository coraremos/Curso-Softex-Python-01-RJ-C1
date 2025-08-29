'''
Exercício 1: Exibindo Itens de uma Lista
1. Crie uma variável chamada frutas e atribua a ela uma lista com 3 nomes de frutas (strings).
2. Use um loop for para percorrer cada item da lista frutas.
3. Dentro do loop, use o print() para exibir o nome de cada fruta em uma nova linha.

Exercício 2: Contando Caracteres de uma Palavra
1. Use o input() para pedir ao usuário que digite uma palavra e guarde-a em uma variável chamada palavra.
2. Use a função len() para contar o número de caracteres da palavra. Guarde o resultado em uma variável chamada tamanho.
3. Use o print() para exibir uma mensagem informando o tamanho da palavra.

Exercício 3: Criando uma Lista com o Usuário
1. Crie uma lista vazia chamada amigos.
2. Crie uma variável chamada contador e defina seu valor inicial como 0.
3. Use um loop while que continue rodando enquanto o contador for menor que 3.
4. Dentro do loop, use o input() para pedir o nome de um amigo e guarde-o em uma variável.
5. Use o método .append() para adicionar o nome do amigo à lista amigos.
6. Aumente o contador em 1 a cada volta do loop.
7. Após o loop, use o print() para exibir a lista completa.

Exercício 4: Imprimindo uma Sequência de Números
1. Use um loop for e a função range() para gerar os números de 1 até 5.
2. Dentro do loop, use o print() para exibir cada número.

Exercício 5: Números Pares com range()
1. Use um loop for e a função range() para gerar os números pares de 2 até 10.
2. Dentro do loop, use o print() para exibir cada número.

Exercício 6: Imprimindo uma Lista de Trás para Frente
1. Crie uma lista com 5 números inteiros.
2. Use um loop for e a função range() para percorrer os índices da lista de trás para frente.
3. Dentro do loop, use o print() para exibir o número correspondente a cada índice.

Exercício 7: Adivinhe o Número
1. Importe o módulo random.
2. Use a função random.randint() para sortear um número entre 1 e 10 e guarde-o em uma variável.
3. Peça ao usuário para adivinhar o número usando o input() e guarde o palpite em uma variável (lembre-se de converter para número com int()).
4. Use uma estrutura if para verificar se o palpite do usuário é igual ao número sorteado.
5. Exiba uma mensagem de "Parabéns!" se ele acertar, ou "Que pena!" se errar, informando qual era o número correto.

Exercício 8: Buscando uma Palavra em uma Frase
1. Peça ao usuário que digite uma frase e guarde-a em uma variável.
2. Peça ao usuário que digite uma palavra e guarde-a em outra variável.
3. Use o operador in dentro de uma estrutura if para verificar se a palavra está contida na frase.
4. Exiba uma mensagem informando se a palavra foi encontrada ou não.

Exercício 9: Somando Elementos de uma Lista
1. Crie uma lista de números.
2. Crie uma variável chamada soma e defina seu valor inicial como 0.
3. Use um loop for para percorrer cada número na lista.
4. Dentro do loop, adicione o valor do número atual à variável soma.
5. Após o loop, exiba o valor final da soma.

Exercício 10: Validando uma Senha Simples
1. Crie duas variáveis, usuario_original e senha_original, com valores pré-definidos.
2. Peça ao usuário para digitar um nome de usuário e uma senha.
3. Use uma estrutura if com a condição e (and) para verificar se o nome de usuário E a senha estão corretos.
4. Exiba uma mensagem de sucesso ou erro.

Exercício 11: Capitalizando Nomes em uma Lista
1. Crie uma lista com 3 nomes, todos em letras minúsculas (ex: ['joão', 'maria', 'pedro']).
2. Crie uma nova lista vazia chamada nomes_formatados.
3. Use um loop for para percorrer a primeira lista.
4. Dentro do loop, use o método .capitalize() em cada nome.
5. Use o método .append() para adicionar o nome formatado à nova lista.
6. Ao final, imprima a lista nomes_formatados.

Exercício 12: Sistema de Login com Tentativas
1. Defina um nome de usuário e uma senha corretos em variáveis.
2. Crie uma variável tentativas com o valor inicial de 3.
3. Use um loop while que continue enquanto o número de tentativas for maior que 0.
4. Dentro do loop, peça o nome de usuário e a senha.
5. Use uma estrutura if para verificar se o login está correto. Se sim, imprima "Login bem-sucedido!" e use o comando break para sair do loop.
6. Se o login estiver incorreto, imprima "Usuário ou senha incorretos." e diminua a variável tentativas em 1.
7. Após o loop, use o if para verificar se as tentativas chegaram a 0. Se sim, imprima "Você excedeu o número de tentativas.".

Exercício 13: Verificador de Palíndromo
1. Peça ao usuário para digitar uma palavra.
2. Use o método .lower() para converter a palavra para minúsculas, garantindo que "Arara" e "arara" sejam tratadas da mesma forma.
3. Crie uma nova variável para guardar a palavra reversa. Uma forma simples é usar fatiamento de string: palavra[::-1].
4. Use uma estrutura if para comparar a palavra original com a palavra reversa.
5. Exiba se a palavra é ou não um palíndromo (uma palavra que se lê da mesma forma de trás para frente).

Exercício 14: Contando Ocorrências de uma Letra
1. Peça ao usuário para digitar uma frase.
2. Peça ao usuário para digitar uma letra.
3. Crie uma variável contador_letras com o valor 0.
4. Use um loop for para percorrer cada caractere da frase.
5. Dentro do loop, use um if para verificar se o caractere atual é igual à letra que o usuário digitou. Use o método .lower() para ignorar maiúsculas e minúsculas.
6. Se for, adicione 1 à variável contador_letras.
7. Ao final do loop, imprima quantas vezes a letra apareceu na frase.

Exercício 15: Sorteando um Aluno para Apresentação
1. Crie uma lista com pelo menos 5 nomes de alunos.
2. Importe o módulo random.
3. Use a função random.choice() para sortear um nome da lista.
4. Exiba uma mensagem dizendo "O aluno sorteado para a apresentação é:" seguido do nome do aluno.

'''