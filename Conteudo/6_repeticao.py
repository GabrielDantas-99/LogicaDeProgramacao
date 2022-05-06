# For:  O laço de repetição FOR é, geralmente, 
# utilizado para intervalos PRÉ-DEFINIDOS. 

x = 5
# Para i(unidade) no intervalo x(5), faça:
for i in range(x): # O 5 não está contido no intervalo
    print(i)       # Mostratá numero de 0 a 4

print()

# Podemos configurar onde o laço iniciará e acabará:
for i in range(3, 7):  
    print(i)       # Mostrará números de 3 a 6

print()

# Podemos definir o intervalo entre cada variável interna(i):
for i in range(0, 11, 2):  
    print(i)       # Mostrará números de 0 a 10 de 2 em 2

print()

# Podemos usar essa estrutura para percorrer strings e listas
capital = "Pernambuco"
for i in capital:
    print(i)

print()

# Podemos ainda juntar uma estrutura de repetição com uma est. condicional
for i in range(0, 100):
    if i % 10 == 0:      # Printando apenas números múltiplos de 10
        print(i)
    else:
        continue