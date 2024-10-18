import os
from abc import *

class Animal(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.nome = None

    def mover(self):
        return "Se movendo"
    
    def informações():
        pass
    
class Cachorro(Animal):
    def __init__(self, nome, raça, dono):
        self.nome = nome
        self.raça = raça
        self.dono = dono

    def mover(self):
        return "Andando de 4 patas"
    
    def informações(self):
        return "Nome: {nome}; \nRaça: {raça}; \nDono: {dono}"
    
class Peixe(Animal):
    def __init__(self, nome, tipo, dono):
        self.nome = nome
        self.tipo = tipo
        self.dono = dono

    def mover(self):
        return "Nadando"
    
    def informações(self):
        return "Nome: {nome}; \nTipo: {tipo}; \nDono: {dono}"
    


