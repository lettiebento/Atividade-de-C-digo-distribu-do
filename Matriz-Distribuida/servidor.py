import socket
import pickle
import numpy as np
import time

HOST = "localhost"
PORT = 5000
BUFFER_SIZE = 4096


def main():
    print("Iniciando servidor...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Servidor aguardando conexão em {HOST}:{PORT} ...")
        conn, addr = server.accept()
        with conn:
            print("Conectado por", addr)
            data = bytearray()
            while True:
                packet = conn.recv(BUFFER_SIZE)
                if not packet:
                    break
                data.extend(packet)
            print("Dados recebidos. Realizando multiplicação...")
            A, B = pickle.loads(data)
            resultado = np.dot(A, B)
            print("Enviando resultado para o cliente...")
            conn.sendall(pickle.dumps(resultado))
            conn.shutdown(socket.SHUT_WR)
            time.sleep(0.5)
    print("Conexão encerrada.")


main()
