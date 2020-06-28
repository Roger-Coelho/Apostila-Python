from funcionario import Funcionario
from gerente import Gerente
from controledebonificacoes import ControleDeBonificacoes
from cliente import Cliente
from conta import Conta
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from diretor import Diretor
from containvestimento import ContaInvestimento

if __name__ == '__main__':

    #funcionario = Funcionario('João', '11111111111-11', 2000.0)
    #print("Bonificações funcionário: {}".format(funcionario.get_bonificacao()))

    #gerente = Gerente("José", "2222222222-22", 5000.0, '1234', 0)
    #print("Bonificações gerente: {}" .format(gerente.get_bonificacao()))

    #controle = ControleDeBonificacoes()
    #controle.registra(funcionario)
    #controle.registra(gerente)

    #print("Total: {}" .format(controle.total_bonificacoes))
    
    #cliente = Cliente("Maria", "3333333333-33", '1234')

    #controle = ControleDeBonificacoes()

    #controle.registra(cliente) c = Conta('123-4', 'João', 1000.0)
    
    #c = Conta('123-4', 'João', 1000.0)
    #cc = ContaCorrente('123-5', 'José', 1000.0)
    #cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    #c.atualiza(0.01)
    #cc.atualiza(0.01)
    #cp.atualiza(0.01)

    #print(c.saldo)
    #print(cc.saldo)
    #print(cp.saldo)
    
    #gerente = Gerente('José', '2222222222-22', 5000.0, '1234', 0)
    #print(gerente.get_bonificacao())

    #diretor = Diretor('João', '1111111111-11', 4000.0)
    #print(diretor.get_bonificacao())
    
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)

    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(cc.saldo)
    print(cp.saldo)
    
    ci = ContaInvestimento('123-6', 'Maria', 1000.0)

    ci.deposita(1000.0)
    ci.atualiza(0.01)
    print(ci.saldo)