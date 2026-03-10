import math
import numpy as np

# Матрица 
A = [[1, -2, 0, -2, -1],
     [-2, -1, 2, -1, -2],
     [5, -3, -2, 1, -3],
     [-1, 0, 2, 2, 2],
     [-1, 2, 1, 6, -1]]

# Вектор правых частей системы
b = [1, 0, 5, 0, 3]

# Размерность системы (количество уравнений)
n = len(b)

# Точность для метода Зейделя
e = 0.01

# Единичная матрица размерности n x n
E = [[int(i == j) for i in range(n)] for j in range(n)]

# Вычисление некоторого значения, связанного с матрицей A и вектором b
dA = sum([sum([b[j] * A[i][j] for j in range(n)]) for i in range(n)])

# Проверка симметричности матрицы A
if all([A[i][j] == A[j][i] for i in range(n) for j in range(n) if i != j]):
    print('Матрица А является симметричной.')
else:
    print('Матрица А не является симметричной.')

# Проверка положительной определённости матрицы A
if dA > 0:
    print('Матрица А является положительно-определённой.')
else:
    print('Матрица А не является положительно-определённой.')



# Функция для метода Гаусса с выбором главного элемента
def gauss_elimination(A, b):

    n = len(b)
    
    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск максимального элемента в текущем столбце
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        
        # Перестановка строк
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        
        # Проверка на вырожденность
        if A[i][i] == 0:
            raise ValueError("Матрица вырожденная. Решение не существует или не единственно.")
        
        # Приведение матрицы к верхнетреугольному виду
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    
    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    
    return x

# Решение СЛАУ методом Гаусса
try:
    x = gauss_elimination(A, b)
    print("Решение СЛАУ Ax = b методом Гаусса с выбором главного элемента:")
    for i, val in enumerate(x):
        print(f"x[{i}] = {val:.5f}")
except ValueError as e:
    print(e)

# Нахождение обратной матрицы методом главных элементов
def inverse(A):

    A = np.array([[1, -2, 0, -2, -1],
     [-2, -1, 2, -1, -2],
     [5, -3, -2, 1, -3],
     [-1, 0, 2, 2, 2],
     [-1, 2, 1, 6, -1]], dtype=float)
    
    n = len(A)  # Размерность матрицы
    E = np.eye(n)  # Единичная матрица того же размера
    
    # Прямой ход метода Гаусса-Жордана
    for i in range(n):
        # Поиск максимального элемента в текущем столбце (главный элемент)
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > abs(A[max_row, i]):
                max_row = k
        
        # Меняем строки местами в A и I
        A[[i, max_row]] = A[[max_row, i]]
        E[[i, max_row]] = E[[max_row, i]]
        
        # Нормализация строки (деление на диагональный элемент)
        pivot = A[i, i]
        if pivot == 0:
            raise ValueError("Матрица вырождена(detA = 0), обратной матрицы не существует.")
        A[i] /= pivot
        E[i] /= pivot
        
        # Обнуление текущего столбца в остальных строках
        for k in range(n):
            if k != i:
                factor = A[k, i]
                A[k] -= factor * A[i]
                print(A[k])
                E[k] -= factor * E[i]
    
    return E

# Вывод обратной матрицы
print("Обратная матрица A^-1 найденая методом главных элементов:")
print(inverse(A))

# Нахождение обратной матрицы с использованием numpy
A = np.array([[1, -2, 0, -2, -1],
     [-2, -1, 2, -1, -2],
     [5, -3, -2, 1, -3],
     [-1, 0, 2, 2, 2],
     [-1, 2, 1, 6, -1]])
n = A.shape[0]
E = np.eye(n)
augmented_matrix = np.hstack((A, E))

# Функция для нахождения обратной матрицы методом главных элементов с использованием numpy
def inverse_by_main_elements(augmented_matrix):
    n = augmented_matrix.shape[0]
    for k in range(n):
        # Поиск максимального элемента в текущем столбце
        max_val = np.abs(augmented_matrix[k:, k]).max()
        max_row = np.where(np.abs(augmented_matrix[k:, k]) == max_val)[0][0] + k
        augmented_matrix[[k, max_row]] = augmented_matrix[[max_row, k]]
        # Исключение элементов
        for i in range(n):
            if i != k:
                augmented_matrix[i] -= augmented_matrix[i, k] / augmented_matrix[k, k] * augmented_matrix[k]
        augmented_matrix[k] /= augmented_matrix[k, k]
    return augmented_matrix[:, n:]

# Вывод обратной матрицы, найденной с использованием numpy
print("Обратная матрица A^-1 найденая методом главных элементов вычисленное стандартными функциями библиотеки numpy:")
print(inverse_by_main_elements(augmented_matrix))

# Вычисление числа обусловленности матрицы A
A = np.array([[1, -2, 0, -2, -1],
     [-2, -1, 2, -1, -2],
     [5, -3, -2, 1, -3],
     [-1, 0, 2, 2, 2],
     [-1, 2, 1, 6, -1]], dtype=float)

# Функция для вычисления евклидовой нормы матрицы
def euclidean_norm(A):
    n = len(A)
    norms = []
    for row in A:
        row_sum = sum(x**2 for x in row)
        norms.append(math.sqrt(row_sum))
    return max(norms)

# Вычисление нормы матрицы A
A_norm = euclidean_norm(A)
# Нахождение обратной матрицы
A_inv = inverse(A)
# Вычисление нормы обратной матрицы
A_inv_norm = euclidean_norm(A_inv)
# Вычисление числа обусловленности
cond_A = A_norm * A_inv_norm
print()
print("Число обусловленности μ матрицы A:", cond_A)

# Вычисление числа обусловленности с использованием numpy
def euclidean_norm(A):
    return np.sqrt(np.max(np.sum(np.abs(A)**2, axis=1)))

cond_A = euclidean_norm(A) * euclidean_norm(np.linalg.inv(A))
print("Число обусловленности μ матрицы A вычисленное стандартными функциями библиотеки numpy:", cond_A)

# Проверка, является ли матрица "удобной" для численных расчётов
if 1 <= cond_A <= 10:
    print("Матрица A является 'удобной' для численных расчетов")
else:
    print("Матрица A является 'неудобной' для численных расчетов")