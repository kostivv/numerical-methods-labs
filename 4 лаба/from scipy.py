from scipy.integrate import quad
import math
import random

# Функция для интегрирования
def function(x):
    """Функция, интеграл которой необходимо вычислить"""
    return x * math.log(x + 2)

# Метод средних прямоугольников
def midpoint_method(a, b, epsilon):
    """Вычисление интеграла методом средних прямоугольников"""
    n = 1  # Начальное количество разбиений
    integral_old = None  # Переменная для хранения предыдущего значения интеграла
    while True:
        h = (b - a) / n  # Шаг разбиения
        integral_new = 0  # Временная переменная для нового значения интеграла
        
        # Вычисление суммы значений функции в средних точках
        for i in range(n):
            x_mid = a + (i + 0.5) * h  # Средняя точка интервала
            integral_new += function(x_mid)
        
        integral_new *= h  # Умножение суммы на шаг для получения приближённого значения интеграла
        
        # Проверка условия выхода
        if integral_old is not None and abs(integral_new - integral_old) < epsilon:
            return integral_new
        
        integral_old = integral_new  # Сохраняем текущее значение для следующей итерации
        n *= 2  # Увеличиваем количество разбиений для повышения точности
        

# Метод Монте-Карло
def monte_carlo_method(a, b, delta):
    """Вычисление интеграла методом Монте-Карло"""
    n = 1  # Начальное количество случайных точек
    integral = 0  # Инициализация переменной для хранения значения интеграла
    while True:
        x_values = [random.uniform(a, b) for _ in range(n)]  # Генерация n случайных точек на интервале [a, b]
        integral_new = (b - a) * sum(function(x) for x in x_values) / n  # Вычисление интеграла как среднее значение функции
        if abs(integral_new - integral) < delta:
            return integral_new
        integral = integral_new
        n *= 2  # Увеличение количества точек для повышения точности

# Метод Симпсона
def simpson_method(a, b, epsilon):
    """Вычисление интеграла методом Симпсона"""
    n = 2  # Начальное количество разбиений (должно быть чётным)
    integral = 0 
    while True:
        h = (b - a) / n  # Шаг разбиения
        integral_new = function(a) + function(b)  # Начальное значение интеграла (граничные точки)
        for i in range(1, n, 2):  # Цикл по нечётным точкам
            integral_new += 4 * function(a + i * h)  # Добавление вклада от нечётных точек с коэффициентом 4
        for i in range(2, n, 2):  # Цикл по чётным точкам
            integral_new += 2 * function(a + i * h)  # Добавление вклада от чётных точек с коэффициентом 2
        integral_new *= h / 3  # Умножение на h/3 для получения приближённого значения интеграла
        if abs(integral_new - integral) < epsilon:
            return integral_new
        integral = integral_new
        n *= 2  # Увеличение количества разбиений для повышения точности

# Параметры интегрирования
a = 1  # Нижний предел интегрирования
b = 2  # Верхний предел интегрирования
epsilon = 1e-4  # Точность для методов средних прямоугольников и Симпсона
delta = 0.05  # Точность для метода Монте-Карло

# Вычисление интеграла с помощью встроенной функции quad()
result_quad, error_quad = quad(function, a, b)

# Вычисление интеграла тремя методами
integral_midpoint = midpoint_method(a, b, epsilon) 
integral_monte_carlo = monte_carlo_method(a, b, delta)
integral_simpson = simpson_method(a, b, epsilon)

# Вывод результатов
print("Результаты вычисления интеграла:")
print(f"1. Встроенная функция quad(): {result_quad:.6f} (оценка погрешности: {error_quad:.6f})")
print(f"2. Метод средних прямоугольников: {integral_midpoint:.6f}")
print(f"3. Метод Монте-Карло: {integral_monte_carlo:.6f}")
print(f"4. Метод Симпсона: {integral_simpson:.6f}")

# Сравнение результатов
print("\nСравнение результатов:")
print(f"Отклонение метода средних прямоугольников от quad(): {abs(result_quad - integral_midpoint):.6f}")
print(f"Отклонение метода Монте-Карло от quad(): {abs(result_quad - integral_monte_carlo):.6f}")
print(f"Отклонение метода Симпсона от quad(): {abs(result_quad - integral_simpson):.6f}")