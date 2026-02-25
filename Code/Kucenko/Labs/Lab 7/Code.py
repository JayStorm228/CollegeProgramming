def F(x):
    return x**4 + 2 * x**2 - x - 1


def dx_F(x):
    return 4 * x**3 + 4 * x - 1


x = 0.0  # вещественный старт
eps = 1e-6
max_iter = 100

for n in range(max_iter):
    fx = F(x)
    dfx = dx_F(x)
    if abs(dfx) < 1e-10:
        print("Производная ≈ 0, стоп")
        break
    x_new = x - fx / dfx
    if abs(x_new - x) < eps:
        print(
            f"""Корень: {x_new:.6f}
F(x) = {F(x_new)}"""
        )
        break
    x = x_new
else:
    print("Не сошлось")
