print(
    """Получите таблицу значений для функции:
    | x**(1/3); x>6
Y = | 2*sin(x); x<5
    | (x+1)**(1/2); 5 <= x <= 6
Отрезок: [2, 12], шаг 0.5"""
)
import math as m

Start = 2.0
Stop = 12
step = 0.5
x = Start
Accuracy = None
while Accuracy == None:
    try:
        Accuracy = int(input("Введите точность вычислений:"))
    except ValueError:
        Accuracy = None
        print(f"Ошибка ввода: {Accuracy} не является числом")
while x <= Stop:
    if x > 6:
        Y = x ** (1 / 3)
    elif x < 5:
        Y = 2 * m.sin(x)
    elif 5 <= x <= 6:
        Y = (x + 1) ** (1 / 2)
    print(f"x: {x}, y: {round(Y, Accuracy)}")
    x += step
