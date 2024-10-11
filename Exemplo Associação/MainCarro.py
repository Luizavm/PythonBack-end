from ClasseCarro import *

m1 = Motor(1.6,"Fiat")
m2 = Motor(2.0,"GM")
m3 = Motor(1.8, "BMW")

r1 = Roda(13, "Pirelle")
r2 = Roda(17, "Dunlop")

c1 = Carro()
c2 = Carro()
c3 = Carro()
c4 = Carro()
c5 = Carro()
c6 = Carro()

c1.setMotor(m1) 
c1.setRoda(r1)

c2.setMotor(m1)
c2.setRoda(r2)

c3.setMotor(m2)
c3.setRoda(r1) 

c4.setMotor(m2)
c4.setRoda(r2) 

c5.setMotor(m3)
c5.setRoda(r1)

c6.setMotor(m3)
c6.setRoda(r2)

print(f"Marca do Carro: {c1.getMotor().getMarcaCarro()}")
print(f"Potencia do Carro: {c1.getMotor().getPotencia()}")
print(f"Marca da roda: {c1.getRoda().getMarcaRoda()}")
print(f"tamanho da roda: {c1.getRoda().getTamanho()}")

print("#######################################")

print(f"Marca do Carro: {c2.getMotor().getMarcaCarro()}")
print(f"Potencia do Carro: {c2.getMotor().getPotencia()}")
print(f"Marca da roda: {c2.getRoda().getMarcaRoda()}")
print(f"tamanho da roda: {c2.getRoda().getTamanho()}")

print("#######################################")

print(f"Marca do Carro: {c3.getMotor().getMarcaCarro()}")
print(f"Potencia do Carro: {c3.getMotor().getPotencia()}")
print(f"Marca da roda: {c3.getRoda().getMarcaRoda()}")
print(f"tamanho da roda: {c3.getRoda().getTamanho()}")

print("#######################################")

print(f"Marca do Carro: {c4.getMotor().getMarcaCarro()}")
print(f"Potencia do Carro: {c4.getMotor().getPotencia()}")
print(f"Marca da roda: {c4.getRoda().getMarcaRoda()}")
print(f"tamanho da roda: {c4.getRoda().getTamanho()}")

print("#######################################")

print(f"Marca do Carro: {c5.getMotor().getMarcaCarro()}")
print(f"Potencia do Carro: {c5.getMotor().getPotencia()}")
print(f"Marca da roda: {c5.getRoda().getMarcaRoda()}")
print(f"tamanho da roda: {c5.getRoda().getTamanho()}")

print("#######################################")

print(f"Marca do Carro: {c6.getMotor().getMarcaCarro()}")
print(f"Potencia do Carro: {c6.getMotor().getPotencia()}")
print(f"Marca da roda: {c6.getRoda().getMarcaRoda()}")
print(f"tamanho da roda: {c6.getRoda().getTamanho()}")