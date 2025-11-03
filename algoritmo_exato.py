import time
from itertools import combinations
import os

# --- Leitura da matriz de adjacência ---
def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            row = [float(x) for x in parts]
            matrix.append(row)
    return matrix

# --- Algoritmo Held-Karp (exato para TSP) ---
def held_karp(matrix):
    n = len(matrix)
    if n == 0:
        return [], 0
    if n == 1:
        return [0], 0

    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = matrix[0][k]

    for s in range(2, n):
        for subset in combinations(range(1, n), s):
            mask = 0
            for bit in subset:
                mask |= 1 << bit
            for j in subset:
                prev_mask = mask ^ (1 << j)
                best = float('inf')
                for k in subset:
                    if k == j:
                        continue
                    best = min(best, C.get((prev_mask, k), float('inf')) + matrix[k][j])
                C[(mask, j)] = best

    full_mask = (1 << n) - 2
    best_cost = float('inf')
    last_node = -1
    for j in range(1, n):
        cost = C.get((full_mask, j), float('inf')) + matrix[j][0]
        if cost < best_cost:
            best_cost = cost
            last_node = j

    tour = [0]
    mask = full_mask
    current = last_node
    for _ in range(n - 1):
        tour.append(current)
        prev = None
        best_prev_cost = float('inf')
        for k in range(1, n):
            if mask & (1 << k):
                prev_cost = C.get((mask ^ (1 << current), k), float('inf')) + matrix[k][current]
                if abs(prev_cost - (best_cost - matrix[current][0])) < 1e-9 or prev_cost < best_prev_cost:
                    prev = k
                    best_prev_cost = prev_cost
        if prev is None:
            break
        mask ^= (1 << current)
        current = prev
    tour.append(0)
    tour.reverse()

    return tour, best_cost

# --- Função para rodar o TSP ---
def tsp_exact_from_file(filename):
    print(f"\n=== Executando TSP exato (Held–Karp) no arquivo: {filename} ===")
    matrix = read_matrix_from_file(filename)
    n = len(matrix)
    print(f"Número de vértices: {n}")

    start_time = time.perf_counter()
    tour, cost = held_karp(matrix)
    end_time = time.perf_counter()

    exec_time = end_time - start_time
    print(f"Caminho ótimo encontrado: {tour}")
    print(f"Custo ótimo: {cost}")
    print(f"Tempo de execução: {exec_time:.6f} segundos")

    return tour, cost, exec_time

# --- Execução principal ---
if __name__ == "__main__":
    arquivo = input(
        "Digite o nome do arquivo .txt da matriz de adjacência (ou pressione Enter para processar todos os arquivos .txt na pasta. Cuidado! os dois ultimos arquivos estouram o limite de ram, ou seja, eles nao podem ser processados.): "
    ).strip()

    if arquivo:
        if os.path.isfile(arquivo):
            tsp_exact_from_file(arquivo)
        else:
            print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        # Processa todos os arquivos .txt na pasta atual
        arquivos_txt = [f for f in os.listdir('.') if f.endswith('.txt')]
        if not arquivos_txt:
            print("Nenhum arquivo .txt encontrado na pasta.")
        for f in arquivos_txt:
            tsp_exact_from_file(f)
