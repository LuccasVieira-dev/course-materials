#Exercício 3: Faça um programa que peça dois números e imprima a soma.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

expressao = f"{n1} + {n2}"

resultado = eval(expressao, {"__builtins__": None}, {})

print(resultado)
