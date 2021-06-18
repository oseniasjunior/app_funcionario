from core import models, database
from datetime import date


f = models.Funcionario()
f.nome = 'Osenias'
f.sexo = 'Masculino'
f.salario = 5000
f.data_nascimento = date(1987, 10, 28)

d = database.Database()
d.save(funcionario=f)


print(d.list())