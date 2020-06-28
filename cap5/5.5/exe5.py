#Exercício 5 modificação

#Função de cálculo da velocidade média 
def velocidade_media(distancia, tempo):
    velocidade = distancia / tempo
    return ("{}".format(velocidade))
    
    
#Teste de exemplo
print(velocidade_media(100, 20))
print(velocidade_media(150, 22))
print(velocidade_media(200, 30))
print(velocidade_media(50, 3))