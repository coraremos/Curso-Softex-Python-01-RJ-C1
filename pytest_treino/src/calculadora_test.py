from faker import Faker
from pytest_treino.src.operations.test.add import AddOperationSpy
from pytest_treino.src.operations.test.sub import SubOperationSpy
from pytest_treino.src.calculadora import Calculadora

fake = Faker()

def test_add():
    addOperation = AddOperationSpy()
    subOperation = SubOperationSpy()
    calculadora = Calculadora(addOperation,subOperation)

    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculadora.add(number1, number2, True) 
    #verificar se vai somar ou se vai retornar None

    #Teste de Entrada
    assert addOperation.soma_attributer['number1'] == number1
    assert addOperation.soma_attributer['number2'] == number2
    #verificar se o dado do espiao chamado chegou 
    
    #Teste de Saída
    assert result is not None


