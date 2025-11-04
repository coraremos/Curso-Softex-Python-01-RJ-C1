from faker import Faker

fake = Faker()

class SubOperationSpy:

    def __init__(self):
        self.diferenca_attributer = {}

    def diferenca(self,number1,number2):
        self.diferenca_attributer['number1'] = number1
        self.diferenca_attributer['number2'] = number2

        return fake.random_number()


#classe Espiã