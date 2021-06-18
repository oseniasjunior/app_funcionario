from core import models
from typing import List


class Database:
    
    def __init__(self) -> None:
        self.caminho = 'c:\\tmp\\funcionarios.txt'

    def save(self, funcionario: models.Funcionario):
        with open(self.caminho, 'a') as arquivo:
            arquivo.write(
                f'nome:{funcionario.nome}|sexo:{funcionario.sexo}|salario:{funcionario.salario}|data_nascimento:{funcionario.data_nascimento}\n'
            )

    def list(self) -> List['models.Funcionario']:        
        funcionarios = []
        with open(self.caminho, 'r') as arquivo:
            linhas = arquivo.readlines()
            for l in linhas:

                funcionario = models.Funcionario()

                for coluna in l.split('|'):
                    key = coluna.split(':')[0]
                    value = coluna.split(':')[1]                     
                    setattr(funcionario, key, value)     

                print(funcionario)

                funcionarios.append(funcionario)

        return funcionarios


