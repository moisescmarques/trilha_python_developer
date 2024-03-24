"""
    Operadores Lógicos
        São operadores utilizados em conjunto com os operadores
        de comparação, para montar uma expressão lógica. Quando
        um operador de comparação é utilizado, o resultado retornado é
        booleano, dessa forma podemos combinar operadores de comparação
        com os operadores lógicos, exemplo:

        op_comparacao + op_logico + op_comparacao...N...
"""

#and: operador E - retorna verdadeiro se ambas condiçoes forem verdadeiras.
#or: operador OU - retorna verdadeiro se uma das condições forem verdadeiras
#not: nega o resutaldo de uma condição. Se True fica False.

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
