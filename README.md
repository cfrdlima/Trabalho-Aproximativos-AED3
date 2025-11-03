
# README – Execução dos Algoritmos TSP

Requisitos

Python 3.8 ou superior instalado no sistema.

VSCode ou outro editor de sua preferência.

Arquivos de matriz de adjacência .txt no mesmo diretório dos scripts.
## Passo 1 – Abrir o terminal

### Navegue até a pasta do projeto:
#### cd /caminho/para/Trabalho-Aproximativos-AED3-main

## Passo 2 – Executar o algoritmo exato
### No terminal, execute:
#### python3 algoritmo_exato.py
#### O programa irá solicitar o nome do arquivo .txt: Digite o nome do arquivo, por exemplo: tsp1_253.txt
#### Ou pressione Enter para processar todos os arquivos .txt da pasta.

O programa exibirá:

Caminho ótimo encontrado

Custo ótimo

Tempo de execução

## Passo 3 – Executar o algoritmo aproximativo
### No terminal, execute:
#### python3 algoritmo_aproximativo.py
#### O programa irá solicitar o nome do arquivo .txt: Digite o nome do arquivo, por exemplo: tsp1_253.txt
####Ou pressione Enter para processar todos os arquivos .txt da pasta.

O programa exibirá:

Melhor rota encontrada

Custo total da rota

Tempo de execução

## Observações importantes

#### Certifique-se de que os arquivos .txt estejam corretamente formatados, com valores numéricos separados por espaços, representando a matriz de adjacência do TSP. O algoritmo exato (Held-Karp) possui complexidade exponencial, então pode demorar muito para matrizes grandes (mais de 15 vértices). O algoritmo aproximativo (Nearest Neighbor + 2-opt) é mais rápido e gera boas soluções para matrizes maiores, mas não garante o custo ótimo. Ambos os scripts suportam a execução em todos os arquivos da pasta caso o usuário pressione Enter sem digitar um arquivo específico.

# Claudinei de Lima e Lyon Falcão
