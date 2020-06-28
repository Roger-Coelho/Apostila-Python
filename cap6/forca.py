#Jogo da forca

import random

#Função do início do jogo.
def jogar():
    
    imprime_mensagem_abertura()
    
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()
    
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
    
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        
        print(letras_acertadas)
    
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
        
       
#Função de Abertura
def imprime_mensagem_abertura():
    print("**********************************")
    print("*** Bem vindo ao jogo da Forca!***")
    print("**********************************")

#Função para carregar a palavra secreta
def carrega_palavra_secreta():

    arquivo = open('cap6\palavras.txt', 'r')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
            
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta

#Função Inicializa letras acertadas
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

#Função que pede o chute
def pede_chute():
    chute = input('Qual letra?')
    chute = chute.strip().upper()
    return chute

#Função marca o chute correto
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

#Função mensagem do vencedor
def imprime_mensagem_vencedor():
    print("Você ganhou!")
    
#Função mensagem do perdedor
def imprime_mensagem_perdedor():
    print("Você perdeu!")
    
print("Fim do jogo")