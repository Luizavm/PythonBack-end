import os

todoslivros = ["Dom Casmurro", "O Alquimista", "1984", "A Revolução dos Bichos", "O Pequeno Príncipe"]
clientes = []
emprestados = []

class Cadastro:

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def retorna(self):
        return f"Cliente: {self.nome} \nCPF: {self.cpf} \nEmail do Cliente: {self.email}"        

class Cadastro_livro:

    def __init__(self, nomelivro, genero):
        self.nomelivro = nomelivro
        self.genero = genero

    def retorliv(self):
        return (f"Nome do livro: {self.nomelivro} \nGênero do livro: {self.genero} \nID do livro: {self.ID}")