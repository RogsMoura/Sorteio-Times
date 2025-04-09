import pandas as pd
import random
import itertools
from copy import deepcopy

# Lê o CSV
df = pd.read_csv("jogadores.csv", sep=';')

# Filtra só os que compareceram
presentes = df[df['compareceu'] == 1].copy()

# Verifica se temos exatamente 20 jogadores
if len(presentes) != 20:
    raise ValueError("Este script espera exatamente 20 jogadores presentes.")

# Cria a lista de jogadores como tuplas (nome, nota)
jogadores = list(zip(presentes['nome'], presentes['nota']))

# Número de simulações para buscar o melhor balanceamento
NUM_SIMULACOES = 10000
melhor_balanceamento = None
melhor_desvio = float('inf')

for _ in range(NUM_SIMULACOES):
    random.shuffle(jogadores)
    times = {f"Time {i+1}": [] for i in range(4)}
    
    # Distribui os jogadores (5 por time)
    for i, jogador in enumerate(jogadores):
        times[f"Time {(i % 4) + 1}"].append(jogador)

    # Calcula médias e desvio padrão das médias
    medias = [sum(nota for _, nota in jogadores) / 5 for jogadores in times.values()]
    desvio = max(medias) - min(medias)

    # Verifica se essa distribuição é melhor
    if desvio < melhor_desvio:
        melhor_desvio = desvio
        melhor_balanceamento = deepcopy(times)

# Exibe o melhor resultado encontrado
print("Melhor distribuição encontrada:\n")
for time, jogadores in melhor_balanceamento.items():
    # Ordena os jogadores do time por nota decrescente
    jogadores_ordenados = sorted(jogadores, key=lambda x: x[1], reverse=True)
    nomes_e_notas = [f"{nome} ({nota})" for nome, nota in jogadores_ordenados]
    media = sum(nota for _, nota in jogadores_ordenados) / len(jogadores_ordenados)
    print(f"{time} | Média: {media:.2f} | Jogadores: {', '.join(nomes_e_notas)}")
