#Faça um programa que peça dois números e imprima a soma.

expressao = input("Digite o cálculo: ")

resultado = eval(expressao, {"__builtins__": None}, {})

print(resultado)
