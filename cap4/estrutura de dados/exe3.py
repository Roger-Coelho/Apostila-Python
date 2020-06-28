#Exercício 3

#Variáveis 
id = int(input("Informe a quantidade de números para obter a média: "))
soma = 0
media = 0
i = 0

#Realizando a soma dos valores
for i in range(i, id):
    num = int(input("Informe um número: "))
    soma += num
    i += 1

#Cálculo da média
media = soma / id

#Imprimindo o valor da média
print("A média dos valores é: {}" .format(media))