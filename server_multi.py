import threading
from socket import *
from constCS import *

def executar_requisicao(conn, data):
    """Esta é a thread filha: apenas executa a lógica e devolve a resposta."""
    try:
        msg = data.decode('utf-8')
        n1, n2, op = msg.split(',')
        ops = {'add': '+', 'sub': '-', 'mult': '*', 'div': '/'}
        res = str(eval(f"{n1} {ops[op]} {n2}"))
        conn.send(res.encode('utf-8'))
    except Exception as e:
        conn.send(b"Erro no processamento")
    finally:
        conn.close()

def start_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', PORT))
    s.listen(5)
    print("Servidor MULTI-THREAD (Strict Model) aguardando conexões...")

    while True:
        conn, addr = s.accept()
        
        data = conn.recv(1024)
        
        if data:
            t = threading.Thread(target=executar_requisicao, args=(conn, data))
            t.start()
        else:
            conn.close()

if __name__ == "__main__":
    start_server()
