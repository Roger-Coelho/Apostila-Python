#Exercício 2 com complemento

#Variáveis para o corrências
lista = []
i = 0
id = int(input("Informe a quantidade de usuários que você deseja adicionar: "))


for i in range (i, id):
    nome = input("Informe o nome: ")
    sobrenome = input("Informe o sobrenome: ")
    idade = int(input("Informe a idade: "))

    #Adicionando os nomes dentro da lista
    lista.append(nome)
    lista.append(sobrenome)
    lista.append(idade)

#Imprimindo a lista
print(lista)