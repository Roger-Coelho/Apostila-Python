#Exercício 1 lista de estrutura de dados
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maior = lista[0]
menor = lista[0]
par = lista[0]
soma  = 0
ocorrencia = lista[0]
vezes = 0 
i = 1


#soma dos valores negativo
negativo = sum([i for i in lista if i < 0])

for i in range (0, 15):
    #Verifica o maior e menor elemento da lista
    if(lista[i] > maior):
        maior = lista[i]
    if(lista[i] < menor):
        menor = lista[i]
    
    #Verifica quais elementos são pares 
    par = lista[i]
    if(par % 2 == 0):
        print("O elemento {} é par." .format(par))
    
    #Ocorrência do primeiro elemento da lista
    if(ocorrencia == lista[i]):
        vezes += 1
    
    #Utilizado para a soma dos elementos da lista e posteriormente usado no cálculo da média
    soma = soma + lista[i]
    
    #Incremento do elemento "i" para percorrer a lista 
    i += 1

#Média dos elementos da lista
media = soma /15   

#Impressão das informações
print("O maior elemento é: {}" .format(maior))
print("O menor elemento é: {}" .format(menor))
print("O número de ocorrência do primeiro elemento da lista é: {}" . format(vezes)) 
print("A soma dos elementos negativos é: {}" .format(negativo))
print("A média da soma {} dos elementos é: {}" .format(soma, media))