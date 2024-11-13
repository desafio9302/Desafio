#Caso necessário, para realizar os testes
# pode-se aumentar o limite de recursividade no Python
#ao descomentar a declaração abaixo.
#Porém, poderá ocorrer stackoverflow para números excessivamente altos.
# from sys import setrecursionlimit
# setrecursionlimit(int(input("Novo limite: ")))


def get_input() -> int:
    n = input("Digite um valor positivo > 1: ")
    if n.isdigit():
        if int(n) >= 2:
            return int(n)
        else:
            raise Exception("O valor deve ser >= 2")
    else:
        raise Exception("O valor deve ser um dígito")

def primos_linear(n: int = None) -> int:
    #Adiciona-se o 2 à lista como caso base
    if n == None:
        n = get_input()

    primos = [2]
    for i in range(2,n+1):
        #Verifica se i não é divisível por nenhum primo
        #Caso não seja, adiciona à lista de primos
        if all([i % p != 0 for p in primos]):
            primos.append(i)
    return primos

def primos_recursivo(n: int = None, i: int = None, primos: list = None) -> int:
    if n == None:
        n = get_input()

    if i == None:
        #Primeiro número do índice
        i = 2

    #Lista primos passada como parâmetro opcional
    if primos == None:
        primos = [2]
    
    if i > n:
        return primos

    #Verifica se i não é divisível por nenhum primo
    #Caso não seja, adiciona à lista de primos
    if all([i % p != 0 for p in primos]):
        primos.append(i)

    #Realiza a iteração de forma recursiva ao invés de um loop
    return primos_recursivo(n, i+1, primos)

print("Primos recursivo")
print(primos_recursivo())
print("Primos linear")
print(primos_linear())