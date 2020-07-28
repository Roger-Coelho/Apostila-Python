from collections import Counter
from collections import deque
from collections import namedtuple
from conta import Conta

#Exemplo1
# cores = [('1', 'azul'), ('2', 'amarelo'), ('3', 'vermelho'), ('1', 'branco'), ('3', 'verde')]

# cores_favoritas =  defaultdict(lista)

# for chave, valor in cores:
#     cores_favoritas[chave].append(valor)

# print(cores_favoritas)


#Counter
cores = ['amarelo', 'azul', 'azul', 'vermelho', 'azul', 'verde', 'vermelho']

contador = Counter(cores)

print(contador)

#Deque

fila = deque()

fila.append('1')
fila.append('2')
fila.append('3')

print(len(fila))    #saída: 3

fila.pop() #exclui elemento da direita

fila.append('3') #adiciona elemento na direita

fila.popleft()  #exclui elemento da esquerda

fila.appendleft('1') #adiciona elemento na esquerda

#namedtuple
Conta = namedtuple('Conta', 'numero titular saldo limite')
conta = Conta('123-4', 'João', 1000.0, 1000.0)

print(conta[0])