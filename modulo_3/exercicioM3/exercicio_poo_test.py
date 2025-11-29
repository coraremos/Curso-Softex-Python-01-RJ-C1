import pytest
from exercicio_poo import Usuario, Email, SMS, SistemaAlerta

@pytest.fixture
def usuario_padrao():
    return Usuario("Tester", "teste@empresa.com")

def test_criacao_usuario(usuario_padrao):
    """Testa se o usuário inicia com os dados corretos."""
    assert usuario_padrao.nome == "Tester"
    assert usuario_padrao.email == "teste@empresa.com"

def test_bloqueio_email_invalido(usuario_padrao, capsys):
    """Testa se o setter bloqueia email sem @ e imprime erro."""
    usuario_padrao.email = "email_ruim.com"
    captured = capsys.readouterr()
    assert usuario_padrao.email == "teste@empresa.com"
    assert "🚫 Erro" in captured.out

def test_alteracao_email_valido(usuario_padrao, capsys):
    """Testa se o setter aceita email com @."""
    usuario_padrao.email = "novo@empresa.com"
    
    captured = capsys.readouterr()
    
    assert usuario_padrao.email == "novo@empresa.com"
    assert "✅ Sucesso" in captured.out

def test_canal_email_saida(capsys):
    """Testa se a classe Email imprime a mensagem correta."""
    canal = Email()
    canal.enviar("Teste Msg")
    captured = capsys.readouterr()
    assert "📧 Enviando para servidor de email: Teste Msg" in captured.out

def test_canal_sms_saida(capsys):
    """Testa se a classe SMS imprime a mensagem correta."""
    canal = SMS()
    canal.enviar("Teste Msg")
    captured = capsys.readouterr()
    assert "📱 Enviando para operadora telefônica: Teste Msg" in captured.out

def test_sistema_alerta_integracao_completa(usuario_padrao, capsys):
    """
    Testa o fluxo completo: Sistema recebe Usuário + Canal e dispara.
    """
    canal = SMS()
    sistema = SistemaAlerta(usuario_padrao, canal)
    
    sistema.disparar("Servidor OK")
    
    captured = capsys.readouterr()
    
    assert "Tester" in captured.out
    # Verifica se a lógica do SMS foi acionada
    assert "📱 Enviando para operadora telefônica: Servidor OK" in captured.out