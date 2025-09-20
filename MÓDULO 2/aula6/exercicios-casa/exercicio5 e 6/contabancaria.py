class ContaBancaria:

    def __init__(self, titular:str, saldo:float) -> None:
        self.titular = titular
        self.saldo = saldo
    
#Crie um método depositar(valor) que some um valor ao saldo da conta. 
#Crie um objeto, deposite um valor e imprima o novo saldo.
    def depositar(self, deposito:float) -> None:
        if deposito == 0:
            print('Nenhum valor foi depositado.')
        self.saldo = self.saldo + deposito
        print(f"Depósito de {deposito} realizado com sucesso.\nSeu saldo agora é de: R${self.saldo:.2f}")
        
        
#Este método deve verificar se há saldo suficiente na conta.
#● Se houver, ele deve subtrair o valor do saldo e imprimir "Saque realizado com sucesso.".
#● Se não houver, ele deve imprimir "Saldo insuficiente." e não alterar o saldo. 
#Teste os dois cenários: um saque bem-sucedido e uma tentativa de sacar mais do que tem.
    def sacar(self, saque:float) -> None:
        if saque < self.saldo:
            print('Não há saldo suficiente para esse saque')
        self.saldo = self.saldo - saque
        print("Saque de R${saque:.2f} realizado.\nSeu saldo atual é de R${self.saldo:.2f}")
        



