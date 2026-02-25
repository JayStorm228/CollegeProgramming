import math as m

x, y, z = 1.825, 18.225, 3.298
Accuracy = 4

y = round(abs(x ** (y / x)) - (y / x) ** (1 / 3), Accuracy)
u = round((y - x) * (y - (z / (y - x)) / (1 + (y - x) ** 2)), Accuracy)
print(
    f"""
    Значение y = {y}
    Значение u = {u}"""
)
