import os
from classes import Gato, Cachorro

def menu():
    print("-- Sistema de veterinária --")
    print("01 - Cadastro de animais")
    print("02 - Listar animais")
    print("03 - Consulta")
    print("04 - Sair do sistema")
    print("")
    escolha = int(input("O que deseja? \n--> "))
    return escolha

################################################################
#CASE 1

def cadastro():
    print("-- Cadastro de animais --")
    print("01 - Cachorro")
    print("02 - Gato")
    print("03 - Voltar")
    print("")
    animal = int(input("O que deseja? \n--> "))
    return animal

def animal1():
    os.system("cls")
    print("-- Cadastro de cachorros --")
    nome = input("Infome o nome do cachorro: \n --> ")
    raca = input("Infome a raça do cachorro: \n --> ")
    dono = input("Infome o nome do dono: \n --> ")
    idade = int(input("Infome a idade do cachorro \n--> "))

    cachorro = Cachorro(nome, raca, dono, idade)
            
    print("")
    print("Cachorro cadastrado com sucesso!")
    os.system("pause")
    os.system("cls")

    return cachorro

def animal2():
    os.system("cls")
    print("-- Cadastro de gatos --")
    nome = input("Infome o nome do gato: \n--> ")
    cor = input("Infome a cor do gato: \n--> ")
    dono = input("Infome o nome do cliente: \n--> ")
    idade = int(input("Infome a idade do gato: \n--> "))

    gato = Gato(nome,cor,dono,idade)
            
    print("")
    print("Gato cadastrado com sucesso!")
    os.system("pause")
    os.system("cls")

    return gato

################################################################
#CASE 2
        
def listar():
    print("-- Lista de animais --")
    print("01 - Listar todos os animais")
    print("02 - Listar todos os cachorros")
    print("03 - Listar todos os gatos")
    print("04 - Voltar")
    escolhalist = int(input("Qual opção deseja ? \n--> "))
    os.system("cls")
    return escolhalist

def todosanimais(lista):
    print("-- Lista de todos os animais --\n")
    print("ID\tNOME\tIDADE\tESPECIE")
            

    cont = 1
    for animais in lista:
        print(f"{cont}\t{animais.getNome()}\t{animais.getIdade()}\t{animais.getEspecie()}")
        cont += 1

def listdog(lista):
    print("-- Lista de todos os cachorros --\n")
    print("ID\tNOME\tIDADE\tRAÇA\t\tDONO")            

    cont = 1
    for animais in lista:
        if animais.getEspecie() == "Cachorro":
            print(f"{cont}\t{animais.getNome()}\t{animais.getIdade()}\t{animais.getRaca()}\t\t{animais.getDono()}")
            cont += 1

def listcat(lista):
    print("-- LISTA DE TODOS OS GATOS --\n")
    print("ID\tNOME\tIDADE\tCOR\t\tDONO")            

    cont = 1
    for animais in lista:
        if animais.getEspecie() == "Gato":
            print(f"{cont}\t{animais.getNome()}\t{animais.getIdade()}\t{animais.getCor()}\t\t{animais.getDono()}")
            cont += 1

################################################################
#CASE 3

def consultani():
    print("-- Consultas --")       
    print("01 - Diagnosticar o animal")
    print("02 - Verificar diagnóstico")
    print("03 - Voltar")
    escolhadig = int(input("Qual opção deseja ? \n--> "))
    return escolhadig

def digani(lista):
    print("---- DIAGNOSTICANDO OS ANIMAIS ----")
    print("")
    print("ID\tNOME\tESPECIE")       

    cont = 1
    for animais in lista:
        print(f"{cont}\t{animais.getNome()}\t{animais.getEspecie()}")
        cont += 1

    print("")

    id_sel = int(input("Qual animal deseja consultar ? \n--> "))
    diag = input("informe o diagnostico do animal\n--> ")

    lista[id_sel - 1].setDiag(diag)

    print("")
    print("DIAGNOSTICO CADASTRADO COM SUCESSO")
    os.system("pause")
    os.system("cls")

def verificdig(lista):
    print("-- VERIFICANDO DIAGNOSTICO DO ANIMAL --")
    print("")
    print("ID\tNOME\tESPECIE")       

    cont = 1
    for animais in lista:
        print(f"{cont}\t{animais.getNome()}\t{animais.getEspecie()}")
        cont += 1

    print("")

    id_sel = int(input("Qual animal deseja verificar ? \n--> "))

    print(f"O diagnostico do animal é: {lista[id_sel - 1].getDiag()}\n")
    os.system("pause")
    os.system("cls")
