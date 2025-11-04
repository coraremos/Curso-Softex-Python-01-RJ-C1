from e2 import rotacionar_lista
import pytest

def test_rotacionar_lista():


    lista_de_espera = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono', 'décimo']
    saida = ['décimo', 'primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono']

    assert rotacionar_lista(lista_de_espera,1) == saida