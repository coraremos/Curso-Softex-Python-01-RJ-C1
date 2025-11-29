class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
            print(f"✅ Sucesso: Email alterado para {novo_email}")
        else:
            print(f"🚫 Erro: O email '{novo_email}' é inválido (falta @).")

class CanalEnvio:
    def enviar(self, mensagem):
        raise NotImplementedError("A classe filha deve implementar o método 'enviar'")

class Email(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📧 Enviando para servidor de email: {mensagem}")

class SMS(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📱 Enviando para operadora telefônica: {mensagem}")

class SistemaAlerta:
    def __init__(self, usuario, canal):
        self.usuario = usuario
        self.canal = canal

    def disparar(self, texto):
        print(f"--- Iniciando alerta para {self.usuario.nome} ---")
        self.canal.enviar(texto)
        print("--------------------------------------------------\n")