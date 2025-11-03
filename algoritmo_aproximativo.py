import time
import os

# --- Funções auxiliares ---

def read_matrix_from_file(filename):
    """Lê uma matriz de adjacência a partir de um arquivo .txt."""
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

def cost_of_tour(matrix, tour):
    """Calcula o custo total de um percurso fechado."""
    cost = 0
    n = len(tour)
    for i in range(n - 1):
        cost += matrix[tour[i]][tour[i + 1]]
    cost += matrix[tour[-1]][tour[0]]  # volta ao início
    return cost

def nearest_neighbor(matrix, start=0):
    """Heurística do vizinho mais próximo."""
    n = len(matrix)
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda j: matrix[current][j])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    return tour

def two_opt(matrix, tour):
    """Melhora o percurso usando o algoritmo 2-opt."""
    n = len(tour)
    best_tour = tour[:]
    best_cost = cost_of_tour(matrix, best_tour)
    improved = True

    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue
                new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                new_cost = cost_of_tour(matrix, new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
                    break
            if improved:
                break
    return best_tour, best_cost

# --- Função principal ---
def tsp_approx_from_file(filename):
    print(f"\n=== Executando TSP aproximativo no arquivo: {filename} ===")
    matrix = read_matrix_from_file(filename)
    n = len(matrix)
    print(f"Número de vértices: {n}")

    start_time = time.perf_counter()
    initial_tour = nearest_neighbor(matrix)
    best_tour, best_cost = two_opt(matrix, initial_tour)
    end_time = time.perf_counter()

    exec_time = end_time - start_time
    print(f"Melhor rota encontrada: {best_tour}")
    print(f"Custo total da rota: {best_cost}")
    print(f"Tempo de execução: {exec_time:.6f} segundos")

    return best_tour, best_cost, exec_time

# --- Execução principal ---
if __name__ == "__main__":
    arquivo = input(
        "Digite o nome do arquivo .txt da matriz de adjacência (ou pressione Enter para processar todos os arquivos .txt na pasta): "
    ).strip()

    if arquivo:
        if os.path.isfile(arquivo):
            tsp_approx_from_file(arquivo)
        else:
            print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        arquivos_txt = [f for f in os.listdir('.') if f.endswith('.txt')]
        if not arquivos_txt:
            print("Nenhum arquivo .txt encontrado na pasta.")
        for f in arquivos_txt:
            tsp_approx_from_file(f)
