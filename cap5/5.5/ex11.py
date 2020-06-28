#Exercício 11


def divisao(numero1, numero2):
    if(numero2 !=0):
        resultado = numero1 / numero2
        return resultado
    else:
        print("Não se pode dividir por zero.")

def velocidade_media(espaco, tempo):
    velocidade = divisao(espaco, tempo)
    print("A velocidadade média entre o espaço {} e o tempo {} é: {} " .format(espaco, tempo, velocidade))


velocidade_media(100, 20)
velocidade_media(-20, 10)
velocidade_media(150, 0)