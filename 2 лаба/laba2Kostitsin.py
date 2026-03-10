import matplotlib.pyplot as plt
import math
from sympy import *

def f(x):  # Функция f(x)
    return math.tan(x) + x

def y(i, s):  # Быстрое вычисление значения в нужной точке функции
    return f(s[i])

# Границы интервала интерполяции и количество значений для нахождения корней Чебышёва
a, b, n = 0, 3 * math.pi / 8, 10
Xk = [(a + b) / 2 + (b - a) / 2 * math.cos(math.pi * (0.5 + k) / n) for k in range(n)]
Xa = [0, math.pi / 8, 2 * math.pi / 8, 3 * math.pi / 8]
Xb = [0, math.pi / 8, math.pi / 3, 3 * math.pi / 8]
X = 3 * math.pi / 16

def L(x, s, n):  # Интерполяционный многочлен Лагранжа
    summ = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (x - s[j]) / (s[i] - s[j])
        summ += y(i, s) * p
    return summ

def L_text(x, s, n):  # Интерполяционный многочлен Лагранжа
    summ = 0
    x = Symbol('x')
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (x - s[j]) / (s[i] - s[j])
        summ += y(i, s) * p
    return simplify(summ)

def F(s, n):  # Разделенная разность
    summ = 0
    for j in range(n):
        p = 1
        for i in range(n):
            if i != j:
                p *= (s[j] - s[i])
        summ += y(j, s) / p
    return summ

def P(x, s, n):  # Интерполяционный многочлен Ньютона
    summ = y(0, s)
    for i in range(1, n):
        p = 1
        for j in range(i):
            p *= (x - s[j])
        summ += F(s, i + 1) * p
    return summ

def P_text(x, s, n):  # Интерполяционный многочлен Ньютона
    summ = y(0, s)
    x = Symbol('x')
    for i in range(1, n):
        p = 1
        for j in range(i):
            p *= (x - s[j])
        summ += F(s, i + 1) * p
    return simplify(summ)

# Вывод полиномов
print('Полином Лагранжа:', L_text(X, Xa, n=4))
print('Полином Ньютона:', P_text(X, s=Xb, n=4))
print('Полином Лагранжа по точкам Чебышёва:', L_text(X, s=Xk, n=10))

# Вычисление погрешностей
error_lagrange_a = abs(f(X) - L(X, s=Xa, n=4))
error_newton_b = abs(f(X) - P(X, s=Xb, n=4))
error_lagrange_cheb = abs(f(X) - L(X, s=Xk, n=10))

# Вывод погрешностей в виде чисел
print('Погрешность вычисления многочлена Лагранжа в точке 3*pi/16:', error_lagrange_a)
print('Погрешность вычисления многочлена Ньютона в точке 3*pi/16:', error_newton_b)
print('Погрешность вычисления многочлена Лагранжа по точкам Чебышёва в точке 3*pi/16:', error_lagrange_cheb)

# Генерация значений для графиков
x_vals = [i / 1000 for i in range(0, 1179)]
y_lagrange_a = [L(x, s=Xa, n=4) for x in x_vals]
y_newton_b = [P(x, s=Xb, n=4) for x in x_vals]
y_lagrange_cheb = [L(x, s=Xk, n=10) for x in x_vals]
y_true = [f(x) for x in x_vals]

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_lagrange_a, label='Полином Лагранжа', color = 'red')
plt.plot(x_vals, y_newton_b, label='Полином Ньютона', color = 'blue')
plt.plot(x_vals, y_lagrange_cheb, label='Полином Лагранжа по точкам Чебышёва', color = 'green')
plt.plot(x_vals, y_true, label='Функция f(x)', color = 'brown')

# Добавление точек интерполяции
plt.scatter(Xa, [f(x) for x in Xa], color='red', label='Точки для Лагранжа (Xa)', zorder=5)
plt.scatter(Xb, [f(x) for x in Xb], color='blue', label='Точки для Ньютона (Xb)', zorder=5)
plt.scatter(Xk, [f(x) for x in Xk], color='green', label='Точки Чебышёва (Xk)', zorder=5)

# Настройка графика
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title("График зависимости")
plt.legend()
plt.grid(True)
plt.show()
