import datetime


class Historico:

    # Construtor classe Historico
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    # Método imprime
    def imprime(self):
        print("Data abertura: {}".format(self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)