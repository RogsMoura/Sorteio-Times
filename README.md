🏆 Gerador de Times 
Este script em Python lê uma lista de jogadores de um arquivo CSV, identifica os que compareceram e os distribui em 4 times de 5 jogadores cada, buscando o melhor balanceamento possível entre as 
médias de notas dos times.

📂 Entrada
Um arquivo chamado jogadores.csv, com as seguintes colunas separadas por ponto e vírgula (;):
- nome: nome do jogador
- nota: nota do jogador (ex: avaliação de habilidade)
- compareceu: 1 para presente, 0 para ausente

⚙️ Como funciona
1. Filtra apenas os jogadores presentes.
2. Gera milhares de combinações aleatórias de times.
3. Calcula a média de cada time e escolhe a formação com menor diferença entre as médias.
4. Imprime os times com os jogadores ordenados por nota.

▶️ Como executar
1. Certifique-se de ter o pandas instalado: pip install pandas
2. Execute o script: python sorteio.py
