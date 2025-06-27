import numpy as np
import time
from multiprocessing import Pool, cpu_count

def multiplicacao_sequencial(A, B):
    return np.dot(A, B)

def multiplica_linha(args):
    A, B, linha = args
    return [sum(a * b for a, b in zip(A[linha], col)) for col in zip(*B)]

def multiplicacao_paralela(A, B):
    with Pool(cpu_count()) as p:
        result = p.map(multiplica_linha, [(A, B, i) for i in range(len(A))])
    return result

if __name__ == "__main__":
    A = np.random.randint(0, 10, (100, 100))
    B = np.random.randint(0, 10, (100, 100))

    inicio = time.time()
    multiplicacao_sequencial(A, B)
    fim = time.time()
    tempo_seq = (fim - inicio) * 1000

    inicio = time.time()
    multiplicacao_paralela(A.tolist(), B.tolist())
    fim = time.time()
    tempo_par = (fim - inicio) * 1000

    with open("tempoAlgoritmos.txt", "w", encoding="utf-8") as f:
        f.write(f"Tempo sequencial: {tempo_seq:.2f} ms\n")
        f.write(f"Tempo paralelo: {tempo_par:.2f} ms\n")

    print("Tempos registrados em tempoAlgoritmos.txt")
