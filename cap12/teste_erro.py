# from contacorrente import ContaCorrente

# def metodo1():
#     print("Início do método 1")
#     metodo2()
#     print("Fim do método 1")

# def metodo2():
#     print("Início do método2")
#     cc = ContaCorrente("José", "123", 0)
#     for i in range(1,15):
#         cc.deposita(i + 1000)
#         print(cc.saldo)
#         if(i == 5):
#             cc = None
#     print("Fim do método2")

# if __name__ == '__main__':
#     print("Início do main")
#     try:
#         metodo1()
#     except AttributeError:
#         print("Erro")
#     print("Fim do main")




# class MeuErro(Exception):
#     def __init__(self, valor):
#         self.valor = valor
#     def __str__(self):
#         return repr(self.valor)

# if __name__ == '__main__':
#     try:
#         raise MeuErro(2 * 2)
#     except MeuErro as e:
#         print("Minha exceção ocorreu, valor: {}".format(e.valor))
#     raise MeuErro("Oops!")
       
       
def divisao(x, y):
    try:
        resultado = x / y;
    except ZeroDivisionError:
        print("Divisão por zero")
    finally:
        print("Executando o finally")

if __name__ == '__main__':
    divisao(2, 1)
    divisao(2, 0)
    divisao('2', '1')