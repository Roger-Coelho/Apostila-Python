arquivo = open('cap6\palavras.txt', 'r')
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()