"""
Funcoes em Python
"""

import math

# funcao auxiliar para formatar cabecalhos
def exibeCabecalho(textoParaExibir:str, exibePrimeiraDivisao:bool = True) -> None:
    if exibePrimeiraDivisao:
        print("#" + "-" * 79)
    print(f"{textoParaExibir}")
    print("#" + "-" * 79)    


# definindo o procedimento principal
def main():
    # cabecalho (header)
    exibeCabecalho("Meu programa!")

    # instrucao para o usuario
    exibeCabecalho("Vamos calcular a raiz quadrada!", exibePrimeiraDivisao=False)

    # solicita um numero
    numero = None
    try:
        numero: int = int(input("Informe um número: ") or "1")
    except ValueError:
        numero: int = 1
    except:
        print("ERROR!")

    # tenta calcular
    raiz_quadrada = None
    try:
        raiz_quadrada = math.sqrt(numero)
    except:
        print("ERRO!")

    # instrucao para o usuario
    exibeCabecalho("Resultado do calculo")
    print(f"A raiz quadrada de {numero} eh: {raiz_quadrada}.")


# chamando o procedimento principal quando o script eh executado
main()
