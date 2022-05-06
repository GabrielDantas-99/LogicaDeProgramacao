# As estruturas condicionais servem para testar determinadas condições no programa.
numero = int(input("Digite um numero inteiro: "))  # Lendo um valor e convertendo para inteiro

# if: É a primeira estrutura a ser testada pelo código. 
    # Caso ela seja satisfeita, as demais condições serão descartadas. 
# else: É a última estrutura a ser testada pelo código. 
      # É a única estrutura condicional que não precisa de uma condição. 
      # Caso as condições IF e ELIF  não sejam satisfeitas, a ELSE será testada. 
      # É utilizada apenas uma vez.
if numero > 0: 
    print("O numero é positivo!")

else:
    print("O numero é negativo!")


# elif: É a segunda estrutura a ser testada pelo código. 
# Caso a condição IF não seja satisfeita, a ELIF será testada e 
# as demais condições não serão executadas. 
# Pode ser utilizada mais de uma vez e é necessário operadores de comparação.

numero = int(input("Digite um número referente ao mês do ano: "))

if numero == 1:
    print("Janeiro")
elif numero == 2:
    print("Feveiro")
elif numero == 3:
    print("Março")
elif numero == 4:
    print("Abril")
elif numero == 5:
    print("Maio")
elif numero == 6:
    print("Junho")
elif numero == 7:
    print("Julho")
elif numero == 8:
    print("Agosto")
elif numero == 9:
    print("Setembro")
elif numero == 10:
    print("Outubro")
elif numero == 11:
    print("Novembro")
elif numero == 12:
    print("Dezembro")
else:                     # else sendo utilizado para tratamento de erro                 
    print("Digite um numero entre 1 e 12")

# Operador ternário: Utilizado para escrever uma estrutura condicional de forma resumida
# Estrutura: <expressao1> if <condicao> else <expressao2>
x = int(input("Digite um numero inteiro: "))
print("par" if x % 2 == 0 else "impar")