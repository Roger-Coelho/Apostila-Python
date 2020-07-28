from collections.abc import Container

class Funcionarios(Container, Sized):
    
    _dados = []
    
    def __contains__(self, posicao):
        return self._dados.__contains__(self, posicao)
    
    def __len__(self):
        return len(self._dados)
    
if __name__ == '__main__':
    funcionarios = Funcionarios()