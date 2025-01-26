import csv

# Caminho do arquivo CSV
caminho_arquivo = 'amazon.csv'

# Abrir e ler o arquivo CSV
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)  # Cada linha será uma lista
