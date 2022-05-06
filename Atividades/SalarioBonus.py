"""Faça um programa que leia o nome de um vendedor,
o seu salário fixo e o total de vendas efetuadas por ele no mês 
(em dinheiro). Sabendo que este vendedor ganha 15% de comissão 
sobre suas vendas efetuadas, informar o total a receber no final do mês,
com duas casas decimais."""

nome = input("Nome do vendedor: ")
salario_fixo = float(input("Salario fixo: "))
total_vendas = float(input("Total das vendas: "))

salario = salario_fixo + (total_vendas * 15 / 100)

print(f"TOTAL = R$ {salario:.2f}")