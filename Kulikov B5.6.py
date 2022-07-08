import requests
import numpy as np


def zeigen():
    print(f"  0 1 2")
    for i in range(3):
        zeile = " ".join(spielbrett[i])
        print(f"{i} {zeile}")  # print(f" {spielbrett[0][0]} {spielbrett[0][1]} {spielbrett[0][2]}")


def frage():
    while True:
        zahlen = input("    Ваш код: ").split()
        if len(zahlen) != 2:
            print("Введите 2 координаты! ")
            continue
        x, y = zahlen
        if not (x.isdigit()) or not (y.isdigit):
            print("Введите числа")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or 2 < y:
            print("Координаты вне диапазона")
            continue
        if spielbrett[x][y] != " ":
            print("Клетка занята! ")
        return x, y


def durchsetzen():
    dcode = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
             ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
             ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in dcode:
        symbole = []
        for c in cord:
            symbole.append(spielbrett[c[0]][c[1]])
        if symbole == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbole == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


spielbrett = [[" "] * 3 for i in range(3)]
gang = 0
while True:
    gang += 1
    zeigen()
    if gang % 2 == 1:
        print("Ходит крестик ")
    else:
        print("Ходит нолик ")

    x, y = frage()
    if gang % 2 == 1:
        spielbrett[x][y] = "X"
    else:
        spielbrett[x][y] = "0"
    if durchsetzen():
        print("Победа")
        break
    if gang == 9:
        print("Ничья")
        break
