from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT))
s.listen(1)

print("Servidor rodando e aguardando conexões...")

(conn, addr) = s.accept()
print(f"Conectado a: {addr}")

while True:
    data = conn.recv(1024)
    if not data: 
        break 
    
    mensagem = data.decode('utf-8')
    print(f"Mensagem recebida do cliente: {mensagem}")
    
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

print("Encerrando conexão com o cliente.")
conn.close()
s.close()
