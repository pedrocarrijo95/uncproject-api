import threading

def operacao_io():
    # Simula uma operação I/O bloqueante
    import time
    for i in range(10):
        print('cancelar')
        time.sleep(1)
    #return "Resultado da operação I/O"

def lógica_principal():
    print("Lógica principal em execução")

    # Cria uma nova thread para executar a operação I/O
    thread = threading.Thread(target=operacao_io)
    thread.start()

    # Continua com a lógica principal enquanto a operação I/O é executada em segundo plano
    print("Continuando com a lógica principal")

# Executa a lógica principal
lógica_principal()
