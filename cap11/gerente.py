from funcionario import Funcionario
from autenticavelmixin import AutenticavelMixIn
from horaextramixin import HoraExtraMixIn

class Gerente(Funcionario, AutenticavelMixIn, HoraExtraMixIn):

    def __init__(self, nome, cpf, salario,senha, qtd_Funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_Funcionarios = qtd_Funcionarios

    def get_bonificacao(self):
        return self._salario * 0.15

    def autentica(self, senha):
        if(self._senha ==  senha):
            print("Acesso permitido")
            return True
        else:
            print("Acesso negado")
            return False
