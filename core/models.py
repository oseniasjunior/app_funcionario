class Funcionario:

    def __init__(self, nome = None, sexo = None, salario = None, data_nascimento = None) -> None:
        self.nome = nome
        self.sexo = sexo
        self.salario = salario
        self.data_nascimento = data_nascimento

    
    def __str__(self) -> str:
        return f'{self.nome} - {self.sexo} - {self.salario} - {self.data_nascimento}'
