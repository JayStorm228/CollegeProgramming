import numpy as np

Array = np.random.randint(-10, 10, (20,))
Min_Idx = Array.argmin()
Neg_Values_Idx = np.where(Array < 0)[0]
start, end = Neg_Values_Idx[0] + 1, Neg_Values_Idx[1]
SelectedSum = Array[start:end].sum()

print(
    f"""Array: {Array}
Min Index = {Min_Idx}
Negative Values Position: {Neg_Values_Idx}
Selected sum: {SelectedSum}"""
)
