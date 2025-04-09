import pandas as pd
import os

# Função para ler o arquivo CSV
def ler_csv(arquivo):
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo {arquivo} não foi encontrado.")
        return None
    
    try:
        # Adicionando o parâmetro sep=';' para lidar com arquivos CSV que usam ponto e vírgula
        df = pd.read_csv(arquivo, sep=';')
        
        # Verificando as colunas do arquivo CSV
        print("Colunas encontradas no arquivo CSV:", df.columns.tolist())
        
        # Filtra os jogadores que irão comparecer
        df_presente = df[df['compareceu'] == 1]
        print(f"Jogadores que irão comparecer: {df_presente.shape[0]} jogadores")
        
        return df_presente
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None

# Função para balancear os times
def balancear_times(df):
    # Classificar os jogadores pela nota
    df_sorted = df.sort_values(by='nota', ascending=False)

    # Inicializando os times
    times = {f'Time {i+1}': [] for i in range(4)}
    medias = {f'Time {i+1}': 0 for i in range(4)}  # Média de cada time
    jogadores = df_sorted['nome'].values.tolist()
    notas = df_sorted['nota'].values.tolist()

    # Distribuir os jogadores nos times de forma balanceada
    jogador_nota = list(zip(jogadores, notas))
    
    for jogador, nota in jogador_nota:
        # Encontrar o time com a menor média atual
        time_com_menor_media = min(medias, key=medias.get)
        
        # Atribuir o jogador ao time com a menor média
        times[time_com_menor_media].append((jogador, nota))
        
        # Atualizar a média do time
        medias[time_com_menor_media] += nota

    # Calcular a média final de cada time
    for time in times:
        medias[time] = medias[time] / len(times[time])  # Calcular a média real de cada time
    
    # Verificar se a diferença de médias entre os times é maior que 0.3
    while max(medias.values()) - min(medias.values()) > 0.3:
        print("Diferença de médias entre os times é maior que 0.3. Tentando redistribuir jogadores.")
        # Tentamos redistribuir jogadores para equilibrar os times
        times, medias = redistribuir_jogadores(times, medias)

    return times

# Função para redistribuir jogadores para balancear as médias
def redistribuir_jogadores(times, medias):
    # Ordenar os times pela média
    times_ordenados = sorted(times.items(), key=lambda x: medias[x[0]])
    
    # Pegar o jogador do time com a maior média
    time_com_maior_media = times_ordenados[-1][0]
    time_com_menor_media = times_ordenados[0][0]

    jogador_a_mover = times[time_com_maior_media].pop()
    times[time_com_menor_media].append(jogador_a_mover)
    
    # Recalcular as médias
    medias[time_com_maior_media] = sum([nota for _, nota in times[time_com_maior_media]]) / len(times[time_com_maior_media])
    medias[time_com_menor_media] = sum([nota for _, nota in times[time_com_menor_media]]) / len(times[time_com_menor_media])

    return times, medias

# Função para calcular a média das notas de um time
def calcular_media(time):
    notas = [nota for _, nota in time]
    return sum(notas) / len(notas)

# Função principal
def sortear_times(arquivo):
    # Lê os dados dos jogadores
    df_presente = ler_csv(arquivo)

    if df_presente is None:
        print("Erro ao carregar o arquivo CSV.")
        return

    if len(df_presente) < 20:
        print("Número insuficiente de jogadores para formar 4 times de 5 jogadores.")
        return

    # Balancear os times
    times = balancear_times(df_presente)

    # Mostrar os times formados
    for time, jogadores in times.items():
        media = calcular_media(jogadores)  # Calculando a média das notas do time
        jogadores_nomes = [jogador[0] for jogador in jogadores]  # Extraindo os nomes dos jogadores
        jogadores_str = ', '.join(jogadores_nomes)  # Nomes dos jogadores em uma linha

        print(f"{time} - Média das notas: {media:.2f} | Jogadores: {jogadores_str}")

# Executando o código
arquivo_csv = 'jogadores.csv'  # Nome do arquivo CSV com os dados dos jogadores
sortear_times(arquivo_csv)
