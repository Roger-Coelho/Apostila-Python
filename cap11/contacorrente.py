from conta import Conta
from tributavel import Tributavel

class ContaCorrente(Conta, Tributavel):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10
        
    def get_valor_imposto(self):
        return self._saldo * 0.01