#Faça um programa que peça dois números e imprima a soma.

n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
n3 = input("Digite a terceira nota: ")
n4 = input("Digite a quarta nota: ")

expressao = f"({n1} + {n2} + {n3} + {n4}) / 4"

media = eval(expressao, {"__builtins__": None}, {})

print("A média é:", media)
