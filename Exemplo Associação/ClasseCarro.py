class Carro:
    def __init__(self):
        self.motor = None
        self.roda = None

    def getMotor(self):
        return self.motor
    
    def setMotor(self, motor):
        self.motor = motor

    def getRoda(self):
        return self.roda
    
    def setRoda(self, roda):
        self.roda = roda

class Motor:
    def __init__(self, potencia, marcaCarro):
        self.potencia = potencia
        self.marcaCarro = marcaCarro

    def getPotencia(self):
        return self.potencia
    
    def setPotencia(self, potencia):
        self.potencia = potencia

    def getMarcaCarro(self):
        return self.marcaCarro
    
    def setMarcaCarro(self, marcaCarro):
        self.marcaCarro = marcaCarro

class Roda:
    def __init__(self, tamanho, marcaRoda):
        self.tamanho = tamanho
        self.marcaRoda = marcaRoda

    def getTamanho(self):
        return self.tamanho
    
    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def getMarcaRoda(self):
        return self.marcaRoda
    
    def setMarcaRoda(self, marcaRoda):
        self.marcaRoda = marcaRoda

