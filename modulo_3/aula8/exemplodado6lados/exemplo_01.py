import random

def gerar_id_composto() -> str:
    """Gera um ID composto de 4 dígitos aleatórios (1-9)."""
    d1 = str(random.randint(1, 9))
    d2 = str(random.randint(1, 9))
    d3 = str(random.randint(1, 9))
    d4 = str(random.randint(1, 9))
    return f"{d1}{d2}{d3}{d4}"


def jogar_dado_seis_lados() -> int:
    """Gera um número aleatório entre 1 e 6."""
    return random.randint(1, 6)

def verificar_numero_secreto(palpite:int) -> bool:
    """Tenta adivinhar um número entre 1 e 10, tratando erros internos"""
    try:
        numero_secreto = jogar_dado_seis_lados()
        return palpite == numero_secreto
    except ValueError:
        return False
    
print(verificar_numero_secreto(3))

def numero_eh_valido(numero:int) -> bool:
    """Verifica se o numero está no intervalo válido de um dado (1 a 6)."""
    return 1 <= numero <= 6