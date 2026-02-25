#5
import math as m
a = 1.3
b = 0.318
x = 1.4444
t = 2.1
y = 9*x**2+(m.sin(x)**2)*m.sqrt(a-b)
print(f'Answer y: {round(y,3)}')
z = ((x**t)**1/3)*(a*(x**3))-(x**2)/(m.factorial(2))
print(f'Answer z: {round(z,3)}')
input()
