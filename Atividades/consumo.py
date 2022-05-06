# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida 
# (em Km) e o total de combustível gasto (em litros).

# Distância total percorrida em Km:
x = int(input("Informe a distância total: "))

# Total de combustível gasto
y = float(input("Total de combustível gasto: "))

consumo_medio = x / y 

print(f'{consumo_medio:.3f} km/l')