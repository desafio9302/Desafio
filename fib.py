import math

#Caso necessário, para realizar os testes
# pode-se aumentar o limite de recursividade no Python
#ao descomentar a declaração abaixo.
#Porém, poderá ocorrer stackoverflow para números excessivamente altos.
# from sys import setrecursionlimit
# setrecursionlimit(int(input("Novo limite: ")))

def get_input():
    n = input("Digite um valor positivo: ")
    if n.isdigit():
        if int(n) >= 0:
            return int(n)
        else:
            raise Exception("O valor deve ser >= 0")
    else:
        raise Exception("O valor deve ser um dígito")


def fib_recursivo(n: int = None, l: list = None) -> int:
    #Uma lista l é passada como parâmetro opcional 
    # para evitar a criação de listas novas a cada recursão
    if n == None:
        n = get_input()

    if l == None:
        l = []
   
    if n == 0:
        l.append(0)
    elif n == 1:
        l.extend([0,1])
    else:
        fib_recursivo(n-1, l)
        l.append(l[-1] + l[-2])
    return l

def fib_linear(n: int = None) -> int:
    if n == None:
        n = get_input()
    #Pode-se utilizar a fórmula explicita de Binet
    #https://www.milefoot.com/math/discrete/sequences/binetformula.htm
    return [int((((1 + math.sqrt(5))/2)**i - 
                 ((1 - math.sqrt(5))/2)**i)/math.sqrt(5)) for i in range(n+1)]

print("Fib recursivo")
print(fib_recursivo())
print("Fib linear")
print(fib_linear())