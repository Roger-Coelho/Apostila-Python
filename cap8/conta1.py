from historico import  Historico

class Conta:
    
    #Slots
    __slots__ = ['_numero', '_titular', '_saldo', '_limite','historico']
    
    #Variável da Classe
    _total_contas = 0
    
    #Construtor
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        Conta._total_contas += 1
        self.historico = Historico()
    
    #Property e setter do saldo   
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if(self._saldo < 0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo
    
    #Property e setter do saldo
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    
    #Método da Classe
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
    
     #Método saca
    def saca(self, valor):
        if(self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append("Saque de {}" .format(valor))
    
    #Método extrato
    def extrato(self):
        print("Número: {} \nSaldo: {}" .format(self._numero, self._saldo))
        self.historico.transacoes.append("Tirou extrato - saldo de {}" .format(self._saldo))
        
    #Método deposita
    def deposita(self, valor):
        self._saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))
        
    #Método transfere
    def transfere_para(self, destino, valor):
        
        retirou = self.saca(valor)
        
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferência de {} para conta {}".format(valor, destino._numero))
            return True