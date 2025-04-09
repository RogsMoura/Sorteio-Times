import pandas as pd
import random

# Lê o CSV
df = pd.read_csv("jogadores.csv", sep=';')

# Filtra só os que compareceram
presentes = df[df['compareceu'] == 1].copy()

# Embaralha os jogadores (sem seed fixa, muda a cada execução)
presentes = presentes.sample(frac=1).reset_index(drop=True)

# Ordena por nota decrescente (melhor balanceamento)
presentes = presentes.sort_values(by='nota', ascending=False).reset_index(drop=True)

# Inicializa os times e controle de soma das notas
times = {f"Time {i+1}": [] for i in range(4)}
somas = {f"Time {i+1}": 0 for i in range(4)}

# Aloca cada jogador no time com menor soma atual
for _, jogador in presentes.iterrows():
    # Escolhe o time com menor soma total até agora
    time_escolhido = min(somas, key=somas.get)
    times[time_escolhido].append((jogador['nome'], jogador['nota']))
    somas[time_escolhido] += jogador['nota']

# Exibe os resultados em uma linha por time
for time, jogadores in times.items():
    nomes_e_notas = [f"{nome} ({nota})" for nome, nota in jogadores]
    media = sum(nota for _, nota in jogadores) / len(jogadores)
    print(f"{time} | Média: {media:.2f} | Jogadores: {', '.join(nomes_e_notas)}")
