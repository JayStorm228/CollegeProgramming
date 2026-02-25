import numpy as np

Matrix = np.random.randint(1, 41, (5, 5))
Output = np.triu(Matrix)
print(Output)
