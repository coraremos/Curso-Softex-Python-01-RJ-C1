from exemplo_01 import gerar_id_composto, jogar_dado_seis_lados, verificar_numero_secreto

def test_verificar_numero_secreto(mocker):
    resultado = 5
    resultado_dado = mocker.patch(
        "exemplo_01.jogar_dado_seis_lados",
        return_value=resultado,
    )

    saida = verificar_numero_secreto(5)
    
    assert saida == True

def test_verificar_numero_secreto_falha(mocker):
    resultado = 5
    mock_dado = mocker.patch(
        "exemplo_01.jogar_dado_seis_lados",
        return_value=resultado, # Usamos return_value para um único valor
    )

    saida = verificar_numero_secreto(6)
    
    assert saida == False

def test_verificar_numero_secreto_trata_erro_interno(mocker):
    """
    Testa se verificar_numero_secreto retorna False quando a função interna
    jogar_dado_seis_lados levanta um ValueError.
    """
    # 1. Configurar o Mock para levantar (raise) o erro
    # Usamos side_effect=ValueError para forçar a exceção.
    # O alvo é a função que é chamada dentro do bloco try.
    mock_dado_com_erro = mocker.patch(
        "exemplo_01.jogar_dado_seis_lados",
        side_effect=ValueError("Simulação de erro interno do dado"),
    )

    # 2. Chamar a função
    saida = verificar_numero_secreto(3) # O palpite não importa aqui

    # 3. Asserções
    # O bloco try/except deve capturar o ValueError e retornar False.
    assert saida == False
    # Verifica se a função simulada foi chamada (e gerou o erro)
    mock_dado_com_erro.assert_called_once()

# def test_resultado_dado_seis_lados(mocker):
#     resultado = [1, 2, 3]
#     resultado_mock = mocker.patch(
#         "exemplo_01.random.randint",
#         side_effect=resultado,
#     )
#     assert jogar_dado_seis_lados() == 1
#     assert jogar_dado_seis_lados() == 2
#     assert jogar_dado_seis_lados() == 3


# def test_gerar_id_composto_sequencial(mocker):

#     sequencia_retornos = [1, 5, 9, 2]

#     mock_randint = mocker.patch(
#         "exemplo_01.random.randint", side_effect=sequencia_retornos
#     )

#     resultado = gerar_id_composto()

#     assert resultado == "1592"

#     assert mock_randint.call_count == 4

#     mock_randint.assert_called_with(1, 9)


# def test_gerar_id_composto_limite_maximo(mocker):

#     sequencia_retornos = [9, 9, 9, 9]

#     mock_randint = mocker.patch(
#         "exemplo_01.random.randint", side_effect=sequencia_retornos
#     )

#     resultado = gerar_id_composto()

#     assert resultado == "9999"
#     assert len(resultado) == 4

#     assert mock_randint.call_count == 4

#     #verifica se a primeira chamada da sequencia estava correta
#     mock_randint.call_args_list[0].assert_called_with(1, 9)
#     #'call_args_list[0] -> verifica no índice 0 da lista'

#     #verifica se a última chamada da sequencia estava correta
#     mock_randint.assert_called_with(1, 9)
#     #colocar diretamente o assert verifica somente o último item da lista