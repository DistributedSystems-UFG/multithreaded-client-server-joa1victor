🧮 Tarefa ASR 05 - Cliente-Servidor com Multithreading

Este repositório contém a implementação de um sistema cliente-servidor distribuído, evoluindo a arquitetura básica (ASR 04) para suportar concorrência através de Multithreading em Python (Sockets TCP).

🖥️ Arquitetura do Experimento

O teste de desempenho foi conduzido em um ambiente real de nuvem (AWS EC2), utilizando duas máquinas distintas:

Node 1 (SERVER): responsável por processar as requisições
Node 2 (PEER 1): cliente responsável por gerar carga

A carga consistiu em 500 requisições matemáticas aleatórias.

📊 Resultados e Análise de Desempenho
Cenário	Arquitetura do Servidor	Arquitetura do Cliente	Tempo Total

A	Iterativo (Single-Thread)	Sequencial	-> 0.3655s
B	Concorrente (Multi-Thread)	Sequencial	-> 0.4762s
C	Concorrente (Multi-Thread)	Paralelo (Multi-Thread)	-> 14.5552s

⚙️ Como Reproduzir
Configure o IP do servidor no arquivo constCS.py
Inicie o servidor:
python3 server_single.py   # Cenário A
python3 server_multi.py    # Cenários B e C
Execute os clientes:
python3 client_single.py   # Cenários A e B
python3 client_multi.py    # Cenário C
