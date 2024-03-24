"""#Old style % - 1 forma de interpolação

nome = "Moises"
idade = 22
profissao = "Developer"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, tabalho como %s" 
      "e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

#------------------------------------------------------------------------------------ """

""" #Método format
nome = "Moises"
idade = 22
profissao = "Developer"
linguagem = "Python"


print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {}" 
      " e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1}" 
      " e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

#Método f-string

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

#Formatar strings com f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}") """

#---------------------------------------------------

nome = "João Victor"
idade = 28
profissao = "Programador Progress"
linguagem = "Python"
saldo = 45.4356

dados = {"nome": "João Victor", "idade": 28, "saldo": 45.4352}

#Interpolação com %
print("Nome: %s Idade: %d" % (nome, idade))

#metodo .format
print("Nome: {} Idade: {}".format(nome, idade))

#metodo .format com indices
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

#metodo .format com descrição nas chaves

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {age}" .format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

#f-string
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {dados['nome']} Idade: {dados['idade']} Saldo: {dados['saldo']:.3f}")