import sys


def oneInLine():
    fulano = "FULANO"
    for char in fulano:
        print(char)


def sumNumbers(input):
    sum = 0
    splitedValues = input.split()
    for x in splitedValues:
        if (not x.isdigit):
            err = f"{x} é um valor invalido"
            print(f"Erro ao somar valores, {err}", file=sys.stderr)
        else:
            sum += int(x)

    print(sum)


oneInLine()
sumNumbers(input('digite valores separados por um espaço: \n'))
