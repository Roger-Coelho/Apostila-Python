from funcionario import Funcionario
from gerente import Gerente
from controledebonificacoes import ControleDeBonificacoes
from cliente import Cliente
from conta import Conta
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from diretor import Diretor
from containvestimento import ContaInvestimento
from sistemainterno import SistemaInterno
from manipulador import ManipuladorDeTributaveis
from segurodevida import SeguroDeVida
from tributavel import Tributavel

if __name__ == '__main__':
    
    cc = ContaCorrente('123-4', 'João', 1000.0)
    seguro = SeguroDeVida(100, 'José', '345-77')
    cp = ContaPoupanca('123-6', 'Maria', 200.0)
    
    print(cc.get_valor_imposto())
    print(seguro.get_valor_imposto())
    
    lista_tributaveis = []
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)
    lista_tributaveis.append(cp)
    
    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    
    print(total)