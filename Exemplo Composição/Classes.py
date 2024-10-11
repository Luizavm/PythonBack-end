class Cadastro:
    def __init__(self,nome:str, cpf:int):
        self.nome = nome
        self.cpf = cpf
        self.end = None

    def setEndereco(self, cep:int, N:int, rua:str, bairro:str, cidade:str):
        self.end = Endereco(cep=cep, N=N, rua=rua, bairro=bairro, cidade=cidade )

    def getEndereco(self):
        return self.end
    
    def getRua(self):
        return self.end.getRua()

class Endereco:
    def __init__(self, cep:int, N:int, rua:str, bairro:str, cidade:str):
        self.cep = cep
        self.n = N
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade

    def getRua(self):
        return self.rua

    def __str__(self):
        return str(self.cep)