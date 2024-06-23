import random as rd
import numpy as np
from math import e
from sklearn import datasets

class Perceptron:
    def __init__(self, num, taxa):
        self.num = num
        self.taxa = taxa
        self.gerarXy()
        self.somatório(0)

    def gerarXy(self):
        iris = datasets.load_iris()
        X = iris.data
        y = iris.target
        not_virginica_indices = np.where(y != 2)
        self.X = X[not_virginica_indices]
        self.y = y[not_virginica_indices]

    def functionG(self, u):
        resultado = 1/(1 + e**-u)
        return resultado
    
    def somatório(self, i):
        j = 0
        pesos = []
        pesosTotais = []
        soma = 0
        if(i ==0):
            teta = -1
            while(j != len(self.X)):
                for k in range(4):
                    pesos.append(round(rd.uniform(-1, 1), 2))
                    soma += self.X[j][k]*pesos[k]
                soma += teta 




Ptron = Perceptron(10, 1)
