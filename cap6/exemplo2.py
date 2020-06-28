arquivo = open('cap6\palavras.txt', 'w')
arquivo.write('banana\n')
arquivo.write('melancia\n')
arquivo.write('morango\n')
arquivo.write('manga\n')
arquivo.close()
arquivo = open('cap6\palavras.txt', 'r')
arquivo.read()

for linha in arquivo:
    print(linha)