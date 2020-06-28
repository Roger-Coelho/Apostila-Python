#Exemplo

def teste(arg, *args):
    print("Primeiro argumento normal: {}" .format(arg))
    for arg in args:
        print("Outro argumento: {}" .format(args))
        
teste('python', 'é', 'muito', 'legal')

def minha_funcao(**kwargs):
    for key, value in kwargs.itens():
        print('{0} = {1}'.format(key, value))
        
minha_funcao(nome='caelum')