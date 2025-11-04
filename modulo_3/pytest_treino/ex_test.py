import ex
import pytest

def test_calcular_taxa_desconto(mocker):
    mocker.patch(
        "ex.pegar_taxa_desconto", 
        return_value=0.50,
        ) #retornar desc. 50%

    saida = ex.calcular_taxa_desconto(100) #calcular o desconto para 100 reais

    assert saida == 50 #teste de retorno

def test_calcular_desconto_com_spy_integracao(mocker):
    spy = mocker.spy(ex, "pegar_taxa_desconto") #teste de integracao
    saida = ex.calcular_taxa_desconto(100)
    assert saida == 91.0 #teste de retorno
    spy.assert_called_once() #teste de comportamento
    spy.assert_called_with(0.9) #teste de comportamento

def fake_taxa_desconto(initial_value):
    return 0.40

def test_calcular_desconto_com_spy_e_retorno_customizado(mocker):
    spy = mocker.patch(
        "ex.pegar_taxa_desconto", 
        side_effect=fake_taxa_desconto,
        )
    
    saida = ex.calcular_taxa_desconto(100)

    assert saida == 60.0 #teste de retorno
    spy.assert_called_once() #teste de comportamento
    spy.assert_called_with(0.9) #teste de comportamento

"""
a funcao principal - calcular_desconto()
a funcao dependente - pegar_taxa_desconto()

mocker.patch("nome do arquivo.nome da funcao dependente", return_value="valor")

saída = nomedoaquivo.nomedafuncaoprincipal("valor inserido")
assert saida ==
"""