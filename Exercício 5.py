#Exercício 5: Faça um programa que converta metros para centímetros.

metros = input("Digite a medida em metros: ")
centimetros = eval(metros + " * 100", {"__builtins__": None}, {})

print("O valor em centímetros é:", centimetros)
