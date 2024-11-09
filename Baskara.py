#autor:Nelson Alves
#Date: 05.11.2024
#codigo: Formula de Baskara a,b,c

#importando biblioteca matemática
import math

a=float(input("Digite o valor de a:"))
b=float(input("Digite o valor de b:"))
c=float(input("Digite o valor de c:"))

delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raizes reais")
elif delta == 0:
    raiz = -b / (2*a)
    print("A equação possui uma raiz real e dupla:", raiz)
else: 
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raizes da equação são:")
    print("raiz1 =", raiz1)
    print("raiz2 =", raiz2)
