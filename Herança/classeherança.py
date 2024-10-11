import os


class Conta:
    def __init__(self, nomecad, sobnomecad, cpfcad, saldo):
        self.nomecad = nomecad
        self.sobnomecad = sobnomecad
        self.cpfcad = cpfcad
        self.saldo = saldo

class Contacorrente(Conta):
    def __init__(self, nomecad, sobnomecad, cpfcad, saldo):
        super().__init__(nomecad, sobnomecad, cpfcad, saldo)


        


    


class Contapoupanca(Conta):
    pass






