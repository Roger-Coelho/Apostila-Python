import csv
from sequence import Funcionarios

if __name__ == '__main__':

    arquivo = open('funcionarios.txt', 'r')
    leitor = csv.reader(arquivo)

    funcionarios = Funcionarios()

    for linha in leitor:
        funcionario = Funcionario(linha[0], linha[1], linha[2])
        funcionarios.append(funcionario)

    print('salario - bonificação')

    for c in contas:
        print('{} - {}' .format(f.salario, f.get_bonificacao()))