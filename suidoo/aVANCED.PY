pessoas = ['Ana ',' manuela','FElpe','Pedr0']

print([n for n in range(11) if n % 2 == 0])

pessoas_normalizadas = [pessoas.strip().capitalize() for pessoas in pessoas]
print(pessoas_normalizadas)

dicionario = {
    'nome' : 'Ana',
    'idade' : 80
}

print(dicionario['nome'])

class loteria:
    def __init__(self):
        self.nome = 'Pedro'
        self.numeros = (10,4,5,6,7,25,31)
        
    def total(self):
        return sum(self.numeros)
    

minha_loteria = loteria()
sumtot = minha_loteria.total()

print (f"A soma dos numeros é: {sumtot}")


class funcionario ():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def dados(self):
        return {'nome' : self.nome, 'salario' : self.salario}
    
fabio = funcionario ('Fábio' , 7000)

print(fabio.dados())