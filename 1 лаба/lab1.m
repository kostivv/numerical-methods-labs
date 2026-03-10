clc % Очистка командного окна
clear all
epsilon = 1e-10;
n = 1;
nsum = 0; %инициализация суммы 
while true
    n = n + 1;
    xn = (1/n^3)*nsum; %заданная числовая последовательность
    for j= 1:n
        sum = j^2+nsum;
    end
    nsum = sum;
    xm = (1/n^3)*sum; %подсчет конечного значения
    if abs(xm-xn)<epsilon %проверка критерия Коши
    break;
    end
end
disp([num2str(xn, '%.5f')])

