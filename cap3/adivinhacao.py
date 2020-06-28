numero_secreto = 42
chute = int(input('Digite um número: '))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou")
elif(chute > numero_secreto):
    print("Você errou! O seu chute foi maior que o número secreto!")
elif(chute < numero_secreto):
    print("Você errou! O seu chute foi menor que o número secreto")