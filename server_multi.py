import threading
from socket import *
from constCS import *

def handle_client(conn, addr):
    """Função que roda em uma thread separada para cada cliente."""
    with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            try:
                msg = data.decode('utf-8')
                n1, n2, op = msg.split(',')
                ops = {'add': '+', 'sub': '-', 'mult': '*', 'div': '/'}
                res = str(eval(f"{n1} {ops[op]} {n2}"))
            except:
                res = "Erro"
            conn.send(res.encode('utf-8'))

def start_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', PORT))
    s.listen(5)
    print("Servidor MULTI-THREAD aguardando conexões...")

    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()