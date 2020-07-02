from conta import Conta

class ContaInvestimento(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5