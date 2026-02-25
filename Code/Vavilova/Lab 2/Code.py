import math as m

x = None
a = None
while x == None:  # Вводим ЧИСЛО х
    try:
        x = float(input("Введите число x: "))
    except ValueError:
        print("Вы ввели не число")
        x = None
while a == None:  # Вводим ЧИСЛО а
    try:
        a = float(input("Введите число x: "))
    except ValueError:
        print("Вы ввели не число")
        a = None
y = None
if x < 1:
    y = None
elif x > 1 and x < 2:
    y = None
elif x > 2:
    y = None
elif x == 1 or x == 2:
    print(f"При данном значении х = {x} функция не задана")
print(
    f"""Введённые значения:
      х = {x}
      а = {a}
Значение функции: {y}"""
)
