class Cliente:
    
    # Construtor Cliente
    def __init__(self, nome, sobrenome, cpf):
        # print("inicializa cliente")
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf