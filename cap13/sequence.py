from collections.abc import MutableSequence

class Funcionarios(MutableSequence):
    
    _dados = []
       
    def __len__(self):
        return len(self._dados)
    
    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if(isinstance(valor, Funcionario)):
            self._dados[posicao] = valor
        else:
            raise ValueError('Valor atribuído não é um Funcionario')
        
    def __delitem__(self, posicao):
        return self._dados.insert(posicao, valor)
    
    def insert(self, posicao, valor):
        if(isinstance(valor, Funcionario)):
            return self._dados.insert(posicao, valor)
        else:
            raise ValueError('Valor inserido não é um Funcionario')