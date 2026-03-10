% Функция y = tan(x) + x
func = tan(x) + x;

% Данные для задания a)
X_a = [0, 1.7, 3.4, 5.1];
Y_a = func(X_a);

% Данные для задания b)
X_b = [0, 1.7, 4.0, 5.1];
Y_b = func(X_b);

% Точка для проверки
X_star = 3.0;

% Функция для вычисления многочлена Лагранжа
function L = lagrange_poly(X, Y, x)
    n = length(X);
    L = 0;
    for i = 1:n
        term = Y(i);
        for j = 1:n
            if j ~= i
                term = term * (x - X(j)) / (X(i) - X(j));
            end
        end
        L = L + term;
    end
end

% Функция для вычисления разделенных разностей
function coef = divided_diff(X, Y)
    n = length(X);
    coef = zeros(n, n);
    coef(:,1) = Y';
    for j = 2:n
        for i = 1:n-j+1
            coef(i,j) = (coef(i+1,j-1) - coef(i,j-1)) / (X(i+j-1) - X(i));
        end
    end
    coef = coef(1, :);
end

% Функция для вычисления многочлена Ньютона
function N = newton_poly(coef, X, x)
    n = length(X);
    N = coef(1);
    for i = 2:n
        term = coef(i);
        for j = 1:i-1
            term = term * (x - X(j));
        end
        N = N + term;
    end
end

% Коэффициенты многочлена Ньютона для задания b)
coef_b = divided_diff(X_b, Y_b);

% Вычисление значений интерполяционных многочленов в точке X_star
L_a = lagrange_poly(X_a, Y_a, X_star);
N_b = newton_poly(coef_b, X_b, X_star);

% Истинное значение функции в точке X_star
true_value = func(X_star);

% Погрешности
error_L_a = abs(true_value - L_a);
error_N_b = abs(true_value - N_b);

fprintf('Многочлен Лагранжа (a): значение в точке %.1f = %.4f, погрешность = %.4f\n', X_star, L_a, error_L_a);
fprintf('Многочлен Ньютона (b): значение в точке %.1f = %.4f, погрешность = %.4f\n', X_star, N_b, error_N_b);

% Построение многочлена Лагранжа по 10 точкам Чебышева на интервале [0, 5.1]
n = 10;
chebyshev_nodes = cos((2*(1:n)-1)*pi/(2*n));
chebyshev_nodes = 2.55 * (1 + chebyshev_nodes);  % Масштабирование на интервал [0, 5.1]
Y_c = func(chebyshev_nodes);

L_c = lagrange_poly(chebyshev_nodes, Y_c, X_star);
error_L_c = abs(true_value - L_c);

fprintf('Многочлен Лагранжа по точкам Чебышева (c): значение в точке %.1f = %.4f, погрешность = %.4f\n', X_star, L_c, error_L_c);

% Визуализация
x_vals = linspace(0, 5.1, 400);
y_vals = func(x_vals);

y_L_a = arrayfun(@(x) lagrange_poly(X_a, Y_a, x), x_vals);
y_N_b = arrayfun(@(x) newton_poly(coef_b, X_b, x), x_vals);
y_L_c = arrayfun(@(x) lagrange_poly(chebyshev_nodes, Y_c, x), x_vals);

figure;
plot(x_vals, y_vals, 'k-', 'DisplayName', 'y = tan(x) + x');
hold on;
plot(x_vals, y_L_a, '--', 'DisplayName', 'Лагранж (a)');
plot(x_vals, y_N_b, ':', 'DisplayName', 'Ньютон (b)');
plot(x_vals, y_L_c, '-.', 'DisplayName', 'Лагранж (Чебышев)');
scatter(X_a, Y_a, 'ro');
scatter(X_b, Y_b, 'bo');
scatter(chebyshev_nodes, Y_c, 'go');
legend show;
xlabel('x');
ylabel('y');
title('Интерполяционные многочлены');
grid on;
