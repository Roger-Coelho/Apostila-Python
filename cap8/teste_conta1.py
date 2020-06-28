from conta1 import Conta

conta1 = Conta('123-4', 'José', 1250.0, 1000.0)
conta2 = Conta('123-5', 'João', 7582.0, 1000.0)

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