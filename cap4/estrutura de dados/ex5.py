#Exercício 5

lista = []
id = int(input("Informe quantos usuários deseja adicionar: "))
i = 0

for i in range (i, id):
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Informe a idade: "))
    cidade = input("Informe o nome da cidade: ")

    lista.append(nome)
    lista.append(idade)
    lista.append(cidade)
    
    i += 1

print("Todos os elementos da lista {} " .format(lista))
print("Nome: ", lista.pop(0))
print("Idade: ", lista.pop(1))
print("Cidade: ", lista.pop(2))    