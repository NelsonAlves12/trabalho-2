#autor:Nelson Alves
#Date: 07.11.2024
#codigo: Formula de Baskara a,b,c

#importando biblioteca matemática
import math

def calcular_delta(a, b, c):
    """Calcula o delta da equação de segundo grau."""
    return b**2 - 4*a*c

def calcular_raizes(a, b, delta):
    """Calcula as raízes da equação de segundo grau."""
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2*a)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2

def main():
    """Função principal do programa."""
    while True:
        try:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))

            if a == 0:
                print("Não é uma equação de segundo grau.")
                continue

            delta = calcular_delta(a, b, c)
            raizes = calcular_raizes(a, b, delta)

            if raizes is None:
                print("A equação não possui raízes reais.")
            elif isinstance(raizes, float):
                print("A equação possui uma raiz real e dupla:", round(raizes, 2))
            else:
                print("As raízes da equação são:")
                print("raiz1 =", round(raizes[0], 2))
                print("raiz2 =", round(raizes[1], 2))
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

if __name__ == "__main__":
    main()
