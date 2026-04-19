from socket import *
from constCS import *

def start_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', PORT))
    s.listen(1)
    print("Servidor SINGLE-THREAD aguardando conexões...")

    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data: break
                msg = data.decode('utf-8')
                try:
                    n1, n2, op = msg.split(',')
                    res = str(eval(f"{n1} { {'add':'+','sub':'-','mult':'*','div':'/'}[op] } {n2}"))
                except:
                    res = "Erro"
                
                conn.send(res.encode('utf-8'))

if __name__ == "__main__":
    start_server()