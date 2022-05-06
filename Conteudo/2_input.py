# Para podermos ler dados fornecidos pelo usuário utilizamos a função input()
# Utilizamos essa função dentro de uma variável para armazenar o valor lido
# O input() aceita textos entre aspas para informar o dado que espera receber
nome = input("Qual função ler um dado? ")

# Podemos sobrescrever os valores armazenados em uma mesma variável
nome = input("Digite seu nome: ")    
print(nome)
nome = input("Digite seu sobrenome: ")     # Ao fazer isso, estamos substituindo o valor
print(nome)                                # digitado no primeiro input pelo segundo

# O input, por padrão, converte seus dados lidos em textos.
# Para trabalharmos com numeros, devemos converte-los em números através do CASTING
idade = int(input("Digite sua idade: "))     # 1ª maneira: convertemos na própria variavel

altura = input("Digite sua altura: ")        # 2ª maneira: Lemos o dado e a armazenamos
altura = float(altura)                       # em, seguida, usamos a variavel para fazer o casting

# Para verificarmos o tipo da variável utilizamos o type()
print(type(nome))   # String
print(type(idade))  # Inteiro
print(type(altura)) # Float

# Um quarto tipo de variável é o booleano, que pode ser True ou False
celular_ligado = True
celular_ligado = False
print(type(celular_ligado))