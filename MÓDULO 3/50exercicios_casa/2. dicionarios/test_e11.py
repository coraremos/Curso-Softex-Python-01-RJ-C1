from e11 import contar_palavras

def test_contagem_basica():
    texto = "Olá, mundo! Olá mundo. Teste, teste: exemplo."
    esperado = {"olá": 2, "mundo": 2, "teste": 2, "exemplo": 1}
    assert contar_palavras(texto) == esperado

def test_vazio():
    assert contar_palavras("") == {}

def test_case_e_acentos():
    texto = "Café café CAFÉ"
    assert contar_palavras(texto) == {"café": 3}