"""
Funcoes em Python
"""

import math

# definindo o procedimento principal
def main():
    # cabecalho (header)
    print("#" + "-" * 79)
    print("Meu programa!")
    print("#" + "-" * 79)

    # instrucao para o usuario
    print("#" + "-" * 79)
    print("Vamos calcular a raiz quadrada!")
    print("#" + "-" * 79)

    # solicita um numero
    numero = None
    try:
        numero: int = int(input("Informe um número: ") or "1")
    except ValueError:
        numero: int = 1

    # tenta calcular
    raiz_quadrada = None
    try:
        raiz_quadrada = math.sqrt(numero)
    except:
        print("ERRO!")

    # informacao para o usuario
    print("#" + "-" * 79)
    print("Resultado do calculo")
    print("#" + "-" * 79)
    print(f"A raiz quadrada de {numero} eh: {raiz_quadrada}.")

# chamando o procedimento principal quando o script eh executado
main()
