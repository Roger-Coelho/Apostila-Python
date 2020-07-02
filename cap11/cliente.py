from autenticavelmixin import AutenticavelMixIn

class Cliente(AutenticavelMixIn):
    
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha