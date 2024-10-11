from Classes import *

jose = Cadastro(nome="Jose", cpf=12312312312)
jose.setEndereco(13259128, 10, "R. Senai", "Tamoio", "Varzea")

print(jose.end.rua)
print(jose.end.bairro)

del jose.end

print(jose)

del jose

print(jose)