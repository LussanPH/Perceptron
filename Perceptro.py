import random as rd
import numpy as np
from math import e
from sklearn import datasets

class Perceptron:
    def __init__(self, num, taxa):
        self.num = num
        self.taxa = taxa
        self.gerarXy()

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
        atributos = []
        if(i ==0):
            while(j != len(self.X)):
                atributos.append(self.X[j][0])
                pesos.append(rd.uniform())



Ptron = Perceptron(10, 1)