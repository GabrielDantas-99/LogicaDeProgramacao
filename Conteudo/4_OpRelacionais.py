# A principal função dos Operadores Relacionais é a comparação de variáveis.
# O resultado dessas operações são valores Booleanos(True ou False).

numero_1 = 10
numero_2 = 30

print(numero_1 == numero_2)   # == : Operador de igualdade
print(numero_1 != numero_2)   # != : Operador de Diferenciação
print(numero_1 >= numero_2)   # >= : Operador Maior ou Igual a
print(numero_1 <= numero_2)   # <= : Operador Menor ou Igual a
print(numero_1  > numero_2)   # >  : Operador Maior Que
print(numero_1  < numero_2)   # <  : Operador Menor Que

# Podemos usar operadores lógicos para aninhar comparações entre variáveis:
print(10 == 20 or 10 == 10)   # or:  Uma das comparações precisa ser verdadeira 
print(10 == 20 and 10 == 10)  # and: As duas comparações devem ser verdadeiras
print(not 5 > 3)              # not: Inverte o resultado da comparação
