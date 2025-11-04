# hasher.py
import hashlib


def hash_senha(senha: str) -> str:
    """Gera um hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def verificar_senha(senha_digitada: str, hash_armazenado: str) -> bool:
    """Verifica se a senha digitada corresponde ao hash no banco."""
    return hash_senha(senha_digitada) == hash_armazenado

palavra = 'casa'
segredo = hash_senha(palavra)   
print(segredo)

criptografado = 'b3813027ed2150ec3449f0716cf53c5d4a632486136365bd23e19c372884553f'
print(verificar_senha(palavra,criptografado))

