#Faça um programa em python que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

lado = float(input("Digite o valor do lado do quadrado: "))

area = lado ** 2
dobro_area = area * 2

print(f"A área do quadrado é: {area:g}")
print(f"O dobro desta área é: {dobro_area:g}")
