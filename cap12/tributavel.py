import abc

class Tributavel(abc.ABC):
    
    @abc.abstractclassmethod
    def get_valor_imposto(self):
        pass