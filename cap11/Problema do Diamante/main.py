from classea import A
from classeb import B
from classec import C
from classed import D

if __name__ == '__main__':
    print(D.mro())

    d = D()
    d.m1()
    d.m2()