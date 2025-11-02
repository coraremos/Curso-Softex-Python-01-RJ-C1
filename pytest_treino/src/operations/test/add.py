from faker import Faker

fake = Faker()

class AddOperationSpy:

    def __init__(self):
        self.soma_attributer = {}

    def soma(self,number1,number2):
        self.soma_attributer['number1'] = number1
        self.soma_attributer['number2'] = number2

        return fake.random_number()


#classe Espiã