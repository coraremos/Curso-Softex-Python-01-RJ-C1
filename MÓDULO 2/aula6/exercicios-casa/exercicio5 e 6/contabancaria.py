class ContaBancaria:

    def __init__(self, titular:str, saldo:float) -> None:
        self.titular = titular
        self.saldo = saldo

    def extrato(self) -> None:
        print(f"\nConta bancária de {self.titular} possui saldo de R${self.saldo:.2f}")
    
    def depositar(self, deposito:float) -> None:
        if deposito == 0:
            print('\nNenhum valor foi depositado.')
        self.saldo = self.saldo + deposito
        print(f"\nDepósito de R${deposito:.2f} realizado com sucesso.")
        
    def sacar(self, saque:float) -> None:
        if saque > self.saldo:
            print('\nSaldo insuficiente.')
            return
        self.saldo = self.saldo - saque
        print(f"\nSaque de R${saque:.2f} realizado com sucesso.")
        



