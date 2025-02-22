# -*- coding: utf-8 -*-
"""gráficos_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VrDYObYdJ1LXsfdp_xlpOoA2_1BKqYVP
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.001)
f= np.exp(-x / 10) * np.sin(np.pi * x)
g = x * np.exp(-x / 3)

plt.plot(x, f, label = "F(x)", color = "black",linestyle = "--")
plt.plot(x, g, label = "G(x)",color = "red")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

plt.figure(figsize=(8,6))
plt.subplot(2,1,1)
plt.plot(x, f, label='F(x)')
plt.title('Curva F(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.subplot(2,1,2)
plt.plot(x, g, label='G9x')
plt.title('Curva G(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(x, f, label='f(x) ')
plt.title('Curva f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x, g, label='g(x))')
plt.title('Curva g(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('graficos.jpg')
plt.show()

#2ª questão
def desvendar(y,x):
  y_1 = y
  x_1 = x
  b = 0
  a = 0

  #termo independente
  b = b + y_1[0]
  a  = np.arcsin(y_1[1] - b)/x_1[1]
  return a,b

x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8]
y1 = [5.0, 5.39, 5.72, 5.93, 6.0, 5.91, 5.68, 5.33, 4.94, 4.56, 4.24, 4.05, 4.0, 4.12, 4.37, 4.72, 5.12, 5.49, 5.79, 5.97, 5.99, 5.85, 5.58, 5.22, 4.83]

l = [desvendar(y1,x)]
a = l[0][0]
b = l[0][1]
print(a,b)
print(l)

x1= np.arange(0,5,0.2)
y = np.sin(a * x1) + b

plt.scatter(x,y1,label= " espalhamento", color = "red",)
plt.plot(x1,y, label= " F(x) = seno(ax) + b")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()