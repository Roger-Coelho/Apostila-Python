#Exercício 8 - Calculadora

def calculadora(numero1, numero2):
    resultado = numero1 + numero2
    resultado2 = numero1 - numero2
    print("A soma de {} e {} é: {}" .format(numero1, numero2, resultado))
    print("A subtração de {} e {} é: {}" . format(numero1, numero2, resultado2))

calculadora(10, 5)