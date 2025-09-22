class Produto:
    def __init__(self, nome, preco):
        self._nome = nome #atributo privado, porém acessível
        self.__preco = preco #atributo protegido, não é exibido, dá erro

    @property #transforma em atributo, não precisa parêntese 
    def preco(self):
        return self.__preco
    
    @preco.setter #transforma em forma de método, usando parêntese
    def preco(self, valor):
        if self._verifica_valor(valor):
            self.__preco = valor #se o valor for maior que zero, o preço será atualizado
        else:
            print('valor incorreto!') #se não for, vai informar que é um valor inválido

    def _verifica_valor(self, valor):
        return valor >= 0

caneta = Produto ("Caneta azul", 10)
print(caneta.preco)
caneta.preco = -10