# O comando print() é responsável por exibir dados no console.
# Ele pode ser utilizado para exibir os dados de 3 maneiras:

# 1ª: Concatenação - Usada para juntar apenas strings
idade = input("Digite sua idade: ")
print("Eu tenho " + idade + " anos")

# 2ª: Print Comma(Vírgula): 
nome   = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
print("Meu nome é", nome,  "e tenho", altura, "m de altura")

# 3ª: Print Format: 
altura = float(input("Digite o nome de uma série que você gosta: "))
print("Eu gosto da série {}. Ela é muito legal.".format(altura))

# 3ª: PrintF:
nome  = "Joao" 
idade = 15
print(f'Meu nome é {nome} e tenho {idade} anos')

# Juntamente com o print(), podemos utilizar o \n para quebrar linhas
print("Nome: Joao\nIdade: 15\nAltura: 1.72m")