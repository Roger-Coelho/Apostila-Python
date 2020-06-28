from conta import Conta
from cliente import Cliente

if __name__ == '__main__':

    cliente1 = Cliente('José', 'Silva', '1111111111-11')
    cliente2 = Cliente('Joel', 'Carvalho', '2222222222-22')

    conta1 = Conta('123-4', cliente1, 1250.0, 1000.0)
    conta2 = Conta('123-5', cliente2, 7582.0, 1000.0)

    conta1.extrato()
    conta2.extrato()

    conta1.deposita(100.0)
    conta1.saca(50.0)
    conta1.transfere_para(conta2, 200.0)
    conta1.extrato()

    conta1.historico.imprime()

    conta2.historico.imprime()

    conta2.extrato()

    print(Conta.get_total_contas())