# Importanto Biblioteca Randint
from random import randint

# Fazendo o computador escolher uma opção: 1 - Pedra,2 - Papel, 3 - Tesoura
cpu_choice = randint(1, 3)

# Transformando a escolha da cpu em texto:
if cpu_choice == 1:
  cpu_choice = 'Pedra'
elif cpu_choice == 2:
  cpu_choice = 'Papel'
else:
  cpu_choice = 'Tesoura'

# Interface do jogo:
print('-' * 10)
print("1 - Pedra\n2 - Papel\n3 - Tesoura")
print('-' * 10)

# Lendo a escolha do usuário:
user_choice = int(input("Sua opção: "))

# transformando a escolha do usuario em texto:
if user_choice == 1:
  user_choice = 'Pedra'
elif user_choice == 2:
  user_choice = 'Papel'
else:
  user_choice = 'Tesoura'

# Definindo ganhador:
if user_choice == "Pedra" and cpu_choice == "Tesoura":
  print(f"JOGADOR = {user_choice} x {cpu_choice} = CPU\nVOCÊ GANHOU!")

elif user_choice == "Tesoura" and cpu_choice == "Papel":
  print(f"JOGADOR = {user_choice} x {cpu_choice} = CPU\nVOCÊ GANHOU!")

elif user_choice == "Papel" and cpu_choice == "Pedra":
  print(f"JOGADOR = {user_choice} x {cpu_choice} = CPU\nVOCÊ GANHOU!")

else: 
  print(f"JOGADOR = {user_choice} x {cpu_choice} = CPU\nVOCÊ PERDEU!")