import time
import random
from socket import *
from constCS import *

NUM_REQ = 500

def realizar_requisicao():
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT))
        msg = f"{random.randint(1,100)},{random.randint(1,100)},{random.choice(['add','sub','mult'])}"
        s.send(msg.encode('utf-8'))
        s.recv(1024)
        s.close()
    except:
        pass

if __name__ == "__main__":
    print(f"Iniciando {NUM_REQ} requisições SEQUENCIAIS...")
    start = time.time()
    for _ in range(NUM_REQ):
        realizar_requisicao()
    print(f"Tempo total: {time.time() - start:.4f}s")