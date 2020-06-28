#Exercício 4

#Informações de entrada
nome = input("Digite o nome do usuário: ")
idade = int(input("Informe a idade: "))
cidade = input("Informe o nome da cidade: ")

#Passando as informações para o dicionário
dic = {'nome': nome, 'idade': idade, 'cidade': cidade}

#Exibindo as informações
print("Nome: ", dic['nome'])
print("Idade: ", dic['idade'])
print("Cidade: ", dic['cidade'])