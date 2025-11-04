class Produto:
    def __init__(self, nome, preco):
        self._nome = nome #atributo privado, porém acessível
        self.__preco = preco #atributo protegido, não é exibido, dá erro

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, valor):
        if self._verifica_valor(valor):
            self.__preco = valor #se o valor for maior que zero, o preço será atualizado
        else:
            print('valor incorreto!') #se não for, vai informar que é um valor inválido

    def _verifica_valor(self, valor):
        return valor >= 0

caneta = Produto ("Caneta azul", 0)
print('primeiro get')
print(caneta.get_preco()) #retorna 10!
print('segundo get')
caneta.set_preco(10)
print('terceiro get')
caneta.set_preco(-1)
print(caneta.get_preco())