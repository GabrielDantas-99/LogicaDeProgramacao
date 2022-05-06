"""Calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, 
ao utilizar um automóvel que faz 12 KM/L. Para efetuar o cálculo, deve-se 
fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma
 (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular 
 quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto."""

tempo_gasto = int(input("Tempo gasto: "))
velocidade_media = int(input("Velocidade média: "))

distancia = velocidade_media * tempo_gasto 
consumo = distancia / 12

print(f'{consumo:.3f}')