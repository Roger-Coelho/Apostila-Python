from collections.abc import Container

class Funcionarios(Container):
    _dados = []
    
    def __contains__(self, posicao):
        return self._dados.__contains__(self, posicao)

if __name__ == '__main__':
    Funcionarios = Funcionarios()