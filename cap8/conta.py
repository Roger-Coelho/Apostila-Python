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
    
    #Métodos Get e Set
    #Get e Set do saldo
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        self._saldo = saldo
    
    #Get e Set do titular
    def get_titular(self):
        return self._titular
    
    def set_titular(self, titular):
        self._titular = titular
    
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
        
    #Método Pega Saldo
    def pega_saldo(self):
        return self._saldo