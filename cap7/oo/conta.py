from historico import Historico

class Conta:
    
    #Construtor
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        
        #print("Inicializando uma conta")
        
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    #Método deposita
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))
        
    #Método saca
    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}" .format(valor))
    
    #Método extrato
    def extrato(self):
        print("Número: {} \nSaldo: {}" .format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - saldo de {}" .format(self.saldo))
        
        
    #Método transfere
    def transfere_para(self, destino, valor):
        
        retirou = self.saca(valor)
        
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferência de {} para conta {}".format(valor, destino.numero))
            return True