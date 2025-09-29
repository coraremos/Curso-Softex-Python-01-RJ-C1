'''
7. Carro com Motor e Rodas (Médio)
● Classes: Motor, Roda e Carro.
● Classe Motor:
○ Método: __init__ (sem atributos).
○ Método: ligar() que imprime "Motor ligado.".
● Classe Roda:
○ Método: __init__ (sem atributos).
○ Método: girar() que imprime "A roda está girando.".
● Classe Carro:
○ Atributos (Composição): motor e rodas (uma lista).
○ Método: __init__ que inicializa o motor e cria uma lista com 4 instâncias de Roda.
○ Método: ligar_carro() que chama o método ligar() do motor e, em seguida, itera
sobre a lista rodas para chamar o método girar() de cada uma.

'''