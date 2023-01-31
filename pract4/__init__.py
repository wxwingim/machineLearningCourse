# вариант 14
# Винни-пух, Котенок по имени Гав

import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

# from recommendations import critics
# from recommendations import sim_distance
from recommendations import *

def main():
    os.chdir("/Volumes/data/workspace/Python/machineLearningCource/pract4")
    # print(critics['Дядя Фёдор']['Ну, погоди!'])

    X = []
    y = []
    names = list(critics)
    for cr in range(len(names)):
        try: {
            X.append(critics[names[cr]]['Винни-Пух'])
        }
        except: {
            X.append(-1)
        }

        try: {
            y.append(critics[names[cr]]['Котёнок по имени Гав'])
        }
        except: {
            y.append(0)
        }

    # Вывод графика
    font = {'family': 'Verdana', 'weight': 'normal'}
    rc('font', **font)
    plt.plot(X, y, 'r.', markersize=14)
    plt.title('Критики на координатной плоскости')
    plt.xlabel('Оценка за "Винни-пуха"') # x
    plt.ylabel('Оценка за "Котенка по имени Гав"') # y
    plt.grid()
    plt.show()

    # print("Вызов sim_distance для Телёнок Гаврюша и Почтальон Печкин", sim_distance(critics, 'Телёнок Гаврюша', 'Почтальон Печкин'))
    # print("Вызов sim_distance для Телёнок Гаврюша и Галчонок", sim_distance(critics, 'Телёнок Гаврюша', 'Галчонок'))

    # print("\nВызов sim_pearson для Телёнок Гаврюша и Почтальон Печкин", sim_pearson(critics, 'Телёнок Гаврюша', 'Почтальон Печкин'))
    # print("Вызов sim_pearson для Телёнок Гаврюша и Галчонок", sim_pearson(critics, 'Телёнок Гаврюша', 'Галчонок'))

    print("\nВызов sim_distance для Телёнок Гаврюша и Пёс Шарик", sim_distance(critics, 'Телёнок Гаврюша', 'Пёс Шарик'))
    print("Вызов sim_distance для Кот Матроскин и Галчонок", sim_distance(critics, 'Кот Матроскин', 'Галчонок'))

    print("\nВызов sim_pearson для Телёнок Гаврюша и Пёс Шарик", sim_pearson(critics, 'Телёнок Гаврюша', 'Пёс Шарик'))
    print("Вызов sim_pearson для Кот Матроскин и Галчонок", sim_pearson(critics, 'Кот Матроскин', 'Галчонок'))

    top = top_matches(critics, 'Почтальон Печкин')
    print("\nОтсортированный список", top)

    # наиболее и наименее похожие
    print('\nНаиболее схожий вкус: ' + top[0][0] + ' ' + str(top[0][1]))
    print('Наименее схожий вкус: ' + top[len(top) - 1][0] + ' ' + str(top[len(top) - 1][1]))

    # графики
    critic1 = critics['Почтальон Печкин']
    criticMax = critics[top[0][0]]
    criticMin = critics[top[len(top) - 1][0]]
    films1 = []
    films2 = []
    keys1 = {**critic1, **criticMax}
    keys1 = list(keys1)
    keys2 = {**critic1, **criticMin}
    keys2 = list(keys2)
    x1 = []
    x2 = []
    y1 = []
    y2 =[]

    for key in keys1:
        if key in critic1 and key in criticMax:
            films1.append(key)

    for key in keys2:
        if key in critic1 and key in criticMin:
            films2.append(key)

    for film in films1:
        x1.append(critic1[film])
        y1.append(criticMax[film])

    for film in films2:
        x2.append(critic1[film])
        y2.append(criticMin[film])

    # min
    plt.plot(x1, y1, 'r.', markersize=14)
    plt.title('Оценки общих фильмов для наиболее схожих критиков')
    plt.xlabel('Почтальон Печкин') # x
    plt.ylabel(top[0][0]) # y
    plt.grid()
    xLine = [3, 4]
    yLine = [3.5, 4.5]
    plt.plot(xLine, yLine, 'b-')
    plt.show()

    # max
    plt.plot(x2, y2, 'r.', markersize=14)
    plt.title('Оценки общих фильмов для наименее схожих критиков')
    plt.xlabel('Почтальон Печкин') # x
    plt.ylabel(top[len(top) - 1][0]) # y
    plt.grid()
    xLine = [3, 3.5]
    yLine = [4, 4.5]
    plt.plot(xLine, yLine, 'b-')

    plt.show()

if __name__ == "__main__":
    main()