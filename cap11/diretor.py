from funcionario import Funcionario
from autenticavelmixin import AutenticavelMixIn

class Diretor(Funcionario, AutenticavelMixIn):

    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)
        
    def get_bonificacao(self):
        return self._salario * 0.07