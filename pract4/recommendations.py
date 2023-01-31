import numpy as np

critics = {
        'Кот Матроскин': {
        'Зима в Простоквашино': 2.5,
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 3.0,
        'Винни-Пух': 3.5,
        'Ну, погоди!': 2.5,
        'Котёнок по имени Гав': 3.0
    },
        'Пёс Шарик': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 1.5,
        'Винни-Пух': 5.0,
        'Котёнок по имени Гав': 3.0,
        'Ну, погоди!': 3.5
    },
        'Почтальон Печкин': {
        'Зима в Простоквашино': 2.5,
        'Каникулы в Простоквашино': 3.0,
        'Винни-Пух': 3.5,
        'Котёнок по имени Гав': 4.0
    },
        'Корова Мурка': {
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 3.0,
        'Котёнок по имени Гав': 4.5,
        'Винни-Пух': 4.0,
        'Ну, погоди!': 2.5
    },
        'Телёнок Гаврюша': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 4.0,
        'Ёжик в тумане': 2.0,
        'Винни-Пух': 3.0,
        'Котёнок по имени Гав': 3.0,
        'Ну, погоди!': 2.0
    },
        'Галчонок': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 4.0,
        'Котёнок по имени Гав': 3.0,
        'Винни-Пух': 5.0,
        'Ну, погоди!': 3.5
    },
        'Дядя Фёдор': {
        'Каникулы в Простоквашино': 4.5,
        'Ну, погоди!': 1.0,
        'Винни-Пух': 4.0
    }
}

# метрка схожести
def sim_distance(critics, name1, name2):
    films = [] # общие фильмы

    critic1 = critics[name1]
    critic2 = critics[name2]

    keys = {**critic1, **critic2}
    keys = list(keys)

    for key in keys:
        if key in critic1 and key in critic2:
            films.append(key)

    if len(films) == 0:
        return 0

    c1 = []
    c2 = []
    for film in films:
        c1.append(critic1[film])
        c2.append(critic2[film])

    result = 1 / (1 + np.sqrt(np.sum(np.power(np.array(c1) - np.array(c2), 2))))

    return result

# коэффициент Пирсона
def sim_pearson(critics, name1, name2):
    films = []  # общие фильмы

    critic1 = critics[name1]
    critic2 = critics[name2]

    keys = {**critic1, **critic2}
    keys = list(keys)

    for key in keys:
        if key in critic1 and key in critic2:
            films.append(key)

    if len(films) == 0:
        return 0

    N = len(films)
    X = []
    Y = []
    for film in films:
        X.append(critic1[film])
        Y.append(critic2[film])

    X = np.array(X)
    Y = np.array(Y)

    denominator = np.sqrt((np.sum(X * X) - np.power(np.sum(X), 2) / N)
                          * (np.sum(Y * Y) - np.power(np.sum(Y), 2) / N))

    if denominator == 0:
        return 0

    result = (np.sum(X * Y) - np.sum(X) * np.sum(Y) / N) / denominator

    return result

# метрика схожести
def top_matches(critics, name):
    result = []

    # critics.pop(name)

    # вычисление метрики схожести
    for person in critics:
        if (person == name):
            continue
        dist = sim_pearson(critics, name, person)
        result.append([person, dist])

    # сортировка по убыванию
    result = sorted(result, key=lambda x: x[1], reverse=True)

    return result