#Exercicio de Args e Kwargs

def teste_args_kwargs(*args):
    for arg in args:
        print("arg: ", *args)

args = ('um', 2, 3, 'quatro')
teste_args_kwargs(*args)