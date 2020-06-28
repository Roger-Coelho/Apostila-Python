print('**************************')
print("*   Jogo da Adivinhação  *")
print("**************************")

print("Escolha um dos níveis para a execução de tentativas")

numero_secreto = 42
rodada = 1
total_de_tentativas = 0
total_pontos = 1000

print("**************************")
print("Digite 1 para nível 1")
print("Digite 2 para nível 2")
print("Digite 3 para nível 3") 
nivel = int(input("Digite um nível: "))
print("**************************")

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5

#Comando For
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
    chute_str = int(input("Digite o seu número: "))
    print("Você digitou: ", chute_str)

    acertou = chute_str == numero_secreto
    maior = chute_str > numero_secreto
    menor = chute_str < numero_secreto

    if(acertou):
        print("Você acertou!")
        print("Sua pontuação final é: {}" .format(total_pontos))
        break
    elif(maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
        total_pontos = total_pontos - (chute_str - numero_secreto)
        print("A sua pontuação é: {}" .format(total_pontos))
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
        total_pontos = total_pontos - (numero_secreto - chute_str)
        print("A sua pontuação é: {}" .format(total_pontos))
        
    rodada = rodada + 1    

print("Fim do Jogo!")