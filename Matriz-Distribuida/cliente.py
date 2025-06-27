import socket
import pickle
import numpy as np
import time

HOST = "localhost"
PORT = 5000
BUFFER_SIZE = 4096

print("Gerando matrizes aleatórias...")
A = np.random.randint(0, 10, (100, 100))
B = np.random.randint(0, 10, (100, 100))

print("Conectando ao servidor...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Enviando dados ao servidor...")
    start = time.time()
    client.sendall(pickle.dumps((A, B)))
    client.shutdown(socket.SHUT_WR)
    print("Aguardando resposta do servidor...")
    data = bytearray()
    while True:
        packet = client.recv(BUFFER_SIZE)
        if not packet:
            break
        data.extend(packet)

resultado = pickle.loads(data)
fim = time.time()
tempo_distribuido = (fim - start) * 1000
print(f"Tempo distribuído: {tempo_distribuido:.2f} ms")

with open("tempoAlgoritmos.txt", "a", encoding="utf-8") as f:
    f.write(f"Tempo distribuído: {tempo_distribuido:.2f} ms\n")
