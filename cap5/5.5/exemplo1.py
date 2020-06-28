#Exemplo 1

def velocidade(espaco, tempo):
    v = espaco/tempo
    return v

resultado = velocidade(100, 2)
print(resultado) 
    
def diz_oi():
    print("oi")
    
def dados(nome, idade=None):
    if(idade is not None):
        print("Nome: {} \nidade: {}".format(nome, idade))
    else:
        print("Nome: {} \nIdade:  não informada" .format(nome))
        
        
def calculadora(x, y):
    return {'soma': x+y, 'subtração': x-y}

resultados = calculadora(1, 2)

for key in resultados:
    print('{}: {}' .format(key, resultados[key]))