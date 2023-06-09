import random

"""
🚀 Exercício 1:
Crie um algoritmo não recursivo para contar quantos números pares existem em
uma sequência numérica (1 a n).
"""

randomArr = [
    random.randrange(0, 101) for i in range(random.randrange(0, 50))
]


def notRecursivePairs(arr):
    pairStack = 0
    for number in arr:
        if number % 2 == 0:
            pairStack += 1
    return pairStack


def recursivePairs(arr, number):
    if len(arr) <= 0:
        return number
    else:
        if arr[-1] % 2 == 0:
            newArr = arr.pop(-1)
            return recursivePairs(newArr, number + 1)
        newArr = arr.pop(-1)
        recursivePairs(newArr, number)


print(len(randomArr))
print(
    f"numero de pares na função não recursiva: {notRecursivePairs(randomArr)}"
)
print(recursivePairs(randomArr, 0))
