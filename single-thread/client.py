from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)

try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    
    op = input("Digite a operação (add, sub, div, mult): ").strip().lower()
    
    if op not in ["add", "sub", "div", "mult"]:
        print("Operação inválida. Encerrando o cliente.")
    else:
        mensagem = f"{num1},{num2},{op}"
        s.connect((HOST, PORT))
        s.send(mensagem.encode('utf-8'))
        
        data = s.recv(1024)
        print("Resultado do servidor:", data.decode('utf-8'))

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros válidos.")
except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor. Verifique se ele está rodando.")
finally:
    s.close()
