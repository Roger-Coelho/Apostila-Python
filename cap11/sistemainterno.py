class SistemaInterno:
    
    def login(self, obj):
        if(hasattr(obj, 'autentica')):
            obj.autentica()
            return True
        else:
            print('{} não é autenticável' .format(self.__class__.__name__))
            return False