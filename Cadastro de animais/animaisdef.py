
Pacientes_gatos = []
Pacientes_cachorros = []

class Gato:

    def __init__(self, nome, raça, idade, dono, celdono, proce_medic):
        self.nome = nome
        self.raça = raça
        self.idade = idade
        self.dono = dono
        self.celdono = celdono
        self.proce_medic = ""

    def procedimento_médico(self, procedimento):
        self.procedimento_médico = procedimento
        print(self.procedimento_medico)

class Cachorro:
    
    def __init__(self, nome, raça, idade, dono, celdono, proce_medic):
        self.nome = nome
        self.raça = raça
        self.idade = idade
        self.dono = dono
        self.celdono = celdono
        self.procedimento_medico = ""

    def procedimento_médico(self, procedimento):
        self.proce_medic = procedimento    
        print(self.proce_medic)
        


