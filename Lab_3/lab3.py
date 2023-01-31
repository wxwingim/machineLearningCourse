import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import os

def main():
    # загрузка данных из файла ex1data1.txt
    os.chdir('/Volumes/data/workspace/Python/machineLearningCource/Lab_3')
    data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))
    X = data[:, 0]
    y = data[:, 1]

    # Вывод графика - данные из ex1data2.txt
    font = {'family': 'Verdana', 'weight': 'normal'}
    rc('font', **font)
    plt.plot(X, y, 'b.')
    plt.title('Зависимость прибыльности от численности')
    plt.xlabel('Численность')
    plt.ylabel('Прибыльность')
    plt.grid()
    plt.show()

    # проверка правильности функции compute_cost
    theta = np.matrix('[1; 2]')
    # количество элементов в X
    m = X.shape[0]
    # добавление единичного столбца
    X_ones = np.c_[np.ones((m, 1)), X]
    # print(X_ones[:, 1])
    print('Проверка правильности функции compute_cost: 75.203 = ', compute_cost(X_ones, y, theta))
    # print('gradient_descent: ', gradient_descent(X_ones, y, 0.02, 500))

    # Предсказание для двух городов:
    # получение оптимальных коэффициентов с помощью выборки
    theta = gradient_descent(X_ones, y, 0.02, 500)
    print("Оптимальные коэффициенты: \n", theta)
    # определение городов
    X_test1 = [7.4242, 20.91234] #
    Y_test1 = []
    for i in range(2):
        w0 = theta[0][0]
        wi = theta[1][0]
        yi = w0 + wi * X_test1[i] + 0.01
        Y_test1.append(yi)
    print("Предсказание для двух городов: ", Y_test1)

    # Предсказание
    x = np.arange(min(X), max(X))
    plt.plot(X, y, 'b.')
    plt.plot(X_test1, Y_test1, 'rp', markersize=10)
    plt.title('График линейной зависимости')
    plt.xlabel('Численность')
    plt.ylabel('Прибыльность')
    plt.grid()
    plt.show()

    # Изобажение линии регрессии
    x = np.arange(min(X), max(X))
    plt.plot(X, y, 'b.')
    plt.plot(x, (theta[1]*x + theta[0]).T, 'g--')
    plt.title('График линейной зависимости')
    plt.xlabel('Численность')
    plt.ylabel('Прибыльность')
    plt.grid()
    plt.show()


    # загрузка данных из файла ex1data2.txt
    os.chdir('/Volumes/data/workspace/Python/machineLearningCource/Lab_3')
    data2 = np.matrix(np.loadtxt('ex1data2.txt', delimiter=','))
    m2 = data2.shape[0]

    copyData2 = data2.copy()

    normalTmp = np.zeros((copyData2.shape[1], 2))

    normalTmp[:, 0] = np.mean(copyData2, axis=0)
    normalTmp[:, 1] = np.std(copyData2, axis=0)

    print(normalTmp)

    copyData2 -= normalTmp[:, 0]
    copyData2 /= normalTmp[:, 1]

    X2 = copyData2[:, 0:-1]
    X_ones2 = np.c_[np.ones((X2.shape[0], 1)), X2]
    y2 = copyData2[:, -1]

    theta2 =  gradient_descent(X_ones2, y2, 0.02, 1000)
    print("theta for price: \n", theta2)

    # xyz
    # plot 1
    data2x = data2[:, 0].flatten().tolist()
    data2y = data2[:, 1].flatten().tolist()
    data2z = data2[:, 2].flatten().tolist()

    plt.scatter(data2x, data2y, c=data2z, cmap='gray')

    plt.xlabel("Площадь")
    plt.ylabel("Количество комнат")
    plt.legend("Зависимость цены")

    plt.show()

    # TODO Предсказание для квартир
    X_test2 = np.matrix([[1200, 1], [2710, 3]]) #
    Y_test2 = []
    for i in range(2):
        w0 = theta2[0][0]
        w1 = theta2[1][0]
        w2 = theta2[2][0]
        yi = w0 + w1 * X_test2[i, 0] + w2 * X_test2[i, 1]
        Y_test2.append(yi)
    print("Предсказание для двух городов: ", Y_test2)

    # xyz
    # plot 2
    # theta2 = theta2.T
    x = np.arange(min(data2[:, 0]), max(data2[:, 0]), (max(data2[:, 0])-min(data2[:, 0]))/4)
    # x = np.array([0, ])
    xx = np.arange(min(data2[:, 1]), max(data2[:, 1]))
    plt.scatter(data2x, data2y, c=data2z, cmap='gray')
    # plt.plot(x.reshape(len(x), 1), (theta2[1]*xx + theta2[0]).T, 'g--')
    plt.scatter(X_test2[:, 0].flatten().tolist(), X_test2[:, 1].flatten().tolist(), c=Y_test2, cmap='winter')
    plt.xlabel("Площадь")
    plt.ylabel("Количество комнат")
    plt.legend("Зависимость цены")

    plt.show()

    # 3 метод наименьших квадратов
    X3 = data2[:, 0:-1]
    X_ones3 = np.c_[np.ones((X3.shape[0], 1)), X3]
    y3 = data2[:, -1]

    thetaMNC = np.dot(np.linalg.pinv(np.dot(X_ones3.T, X_ones3)), np.dot(X_ones3.T, y3))
    print("Метод наименьших квадратов: \n", thetaMNC)


# вычисление квадратичной ошибки
def compute_cost(X, y, theta):
    # количество элементов в X
    m = X.shape[0]

    # вычисление гипотезы h0(x)
    h_x = X * theta

    cost = np.sum(np.power(h_x - y, 2)) / 2 / m
    return cost

# градиентный спуск
def gradient_descent(X, y, alpha, iterations):
    # колическтво элементов в X
    m = X.shape[0]

    # количество столбцов в X
    n = X.shape[1]

    # инициализация theta
    theta = np.ones((1, n))
    theta[0][0] = 0
    theta = theta.transpose()
    theta = theta.astype(dtype='float64')

    J_theta = np.zeros(iterations, dtype='float64')
    temp_theta = theta

    for i in range(iterations):
        J_theta[i] = compute_cost(X, y, temp_theta)
        error = (X * temp_theta) - y
        for j in range(n):
            mult = np.sum(np.multiply(error, X[:, j]))
            temp_theta[j][0] = temp_theta[j][0] - alpha * mult / m

    # вывод графика
    plt.plot(np.arange(iterations), J_theta, 'b-')
    plt.title('Снижение ошибки при градиентном спуске')
    plt.xlabel('Ошибка')
    plt.ylabel('Итерация')
    plt.grid()
    plt.show()

    return temp_theta

if __name__ == '__main__':
    main()