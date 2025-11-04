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

caneta = Produto ("Caneta azul", 2.50)
caneta.set_preco(-10) #valor negativo não é aceito na alteração de preço pois não é >= 0. retorna 2.5
caneta.set_preco(10) #retorna 10!
print(caneta.get_preco())

