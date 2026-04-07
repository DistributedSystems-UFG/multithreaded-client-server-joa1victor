from socket import *
from constCS import *
import threading
import time

def lidar_com_cliente(conn, addr):
    """
    Função alvo da thread. Cada cliente conectado ganha uma instância
    desta função rodando em paralelo no processador.
    """
    print(f"Nova conexão iniciada com: {addr}")
    
    while True:
        try:
            data = conn.recv(1024)
            if not data: 
                break 
            
            mensagem = data.decode('utf-8')
            
            # --- GARGALO ARTIFICIAL PARA O EXPERIMENTO ---
            # Simula um cálculo demorado para provar a eficiência da Thread
            time.sleep(0.05) 
            
            try:
                num1_str, num2_str, op = mensagem.split(',')
                
                num1 = int(num1_str)
                num2 = int(num2_str)
                
                if op == "add":
                    resultado = num1 + num2
                elif op == "sub":
                    resultado = num1 - num2
                elif op == "mult":
                    resultado = num1 * num2
                elif op == "div":
                    if num2 == 0:
                        resultado = "Erro: Impossível dividir por zero."
                    else:
                        resultado = num1 / num2
                else:
                    resultado = "Erro: Operação inválida."
                    
                resposta = str(resultado)

            except ValueError:
                resposta = "Erro: Formato de dados incorreto. Certifique-se de enviar inteiros."
            except Exception as e:
                resposta = f"Erro inesperado no servidor: {e}"
                
            conn.send(resposta.encode('utf-8'))
            
        except ConnectionResetError:
            break # Lida com a desconexão abrupta do cliente

    print(f"Encerrando conexão com o cliente {addr}.")
    conn.close()

# ==========================================
# CONFIGURAÇÃO PRINCIPAL DO SERVIDOR
# ==========================================
s = socket(AF_INET, SOCK_STREAM)
# SO_REUSEADDR evita o erro de porta travada caso o servidor seja reiniciado rápido demais
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
s.bind(('0.0.0.0', PORT))

# O listen(100) permite que até 100 clientes fiquem na "fila de espera" do S.O.
# simultaneamente enquanto o accept() não os atende.
s.listen(100) 

print("Servidor Multithread rodando e aguardando conexões...")

# Laço principal: apenas aceita a conexão e delega para a Thread
while True:
    try:
        (conn, addr) = s.accept()
        
        # Dispara uma nova thread executando a função 'lidar_com_cliente'
        thread_cliente = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
        thread_cliente.start()
        
    except Exception as e:
        print(f"Erro ao aceitar conexão: {e}")