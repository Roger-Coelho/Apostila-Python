#Exercício 9 - Calculadora Modificada
print("*********************")
print("*****Calculadora*****")
print("*********************")

def calculadora(numero1, numero2):
    resultado = numero1 + numero2
    resultado2 = numero1 - numero2
    resultado3 = numero1 * numero2
    resultado4 = numero1 / numero2
    
    print("A soma de {} e {} é: {}" .format(numero1, numero2, resultado))
    print("A subtração de {} e {} é: {}" . format(numero1, numero2, resultado2))
    print("A multiplicação de {} e {} é: {}" . format(numero1, numero2, resultado3))
    print("A divisão de {} e {} é: {}" . format(numero1, numero2, resultado4))


num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))


calculadora(num1, num2)