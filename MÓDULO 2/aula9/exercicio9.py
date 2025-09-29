'''
9. Conta Bancária (Médio/Difícil)
● Classes: Cliente, Transacao e ContaCorrente.
● Classe Cliente:
○ Atributos: nome e cpf.
○ Método: __init__(nome, cpf).
● Classe Transacao:
○ Atributos: tipo (string, ex: "deposito", "saque"), valor e data (pode ser uma string
simples ou um objeto datetime).
○ Método: __init__(tipo, valor, data).
● Classe ContaCorrente:
○ Atributos (Composição): cliente (um objeto Cliente), saldo e historico (uma lista
vazia de Transacao).
○ Método: __init__(cliente, saldo).
○ Método: sacar(valor) que subtrai o valor do saldo e cria uma Transacao negativa no
histórico.
○ Método: depositar(valor) que adiciona o valor ao saldo e cria uma Transacao
positiva no histórico.
○ Método: mostrar_historico() que imprime cada transação na lista.

'''