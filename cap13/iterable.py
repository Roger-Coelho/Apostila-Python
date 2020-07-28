from collections.abc import Container

class Funcionarios(Container, Sized, Iterable):
    
    _dados = []
    
    def __contains__(self, posicao):
        return self._dados.__contains__(self, posicao)
    
    def __len__(self):
        return len(self._dados)
    
    def __iter__(self):
        return self._dados.__iter__(self)
    
if __name__ == '__main__':
    funcionarios = Funcionarios()