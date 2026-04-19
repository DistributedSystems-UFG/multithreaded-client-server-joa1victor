import threading
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
    print(f"Disparando {NUM_REQ} threads em PARALELO...")
    threads = []
    start = time.time()
    
    for _ in range(NUM_REQ):
        t = threading.Thread(target=realizar_requisicao)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join() #Espera todas terminarem para fechar o tempo
        
    print(f"Tempo total: {time.time() - start:.4f}s")