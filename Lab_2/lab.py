import numpy as np
import scipy.io
from sklearn import svm
from collections import OrderedDict

from process_email import process_email
from process_email import email_features
from process_email import get_dictionary


def main():
    with open('email.txt', 'r') as file:
        email = file.read().replace('\n', '')
    print(email)

    print(process_email(email))
    features = email_features(process_email(email))

    print('Длина вектора признаков: 1899')
    pr = sum(features > 0)
    print('Количество ненулевых элементов: %f' % pr)

    data = scipy.io.loadmat('train.mat')
    X = data['X']
    y = data['y'].flatten()

    print('Тренировка SVM-классификатора с линейным ядром...')
    clf = svm.SVC(C=0.1, kernel='linear', tol=1e-3)
    model = clf.fit(X, y)
    p = model.predict(X)

    # res = sum(p == y) / len(y) * 100
    res = (p == y).mean() * 100
    print('Точность на обучающей выборке: ' + str(res))

    data = scipy.io.loadmat('test.mat')
    X = data['Xtest']
    y = data['ytest'].flatten()
    p = model.predict(X)
    res = (p == y).mean() * 100
    print('Точность на тестовой выборке: ' + str(res))

    t = sorted(list(enumerate(model.coef_[0])), key=lambda e: e[1], reverse=True)
    d = OrderedDict(t)
    idx = list(d.keys())
    weight = list(d.values())
    dictionary = get_dictionary()

    print('Топ-15 слов в письмах со спамом: ')
    for i in range(15):
        print(' %-15s (%f)' %(dictionary[idx[i]], weight[i]))

    with open('goodmail.txt', 'r') as file:
        goodmail = file.read().replace('\n', '')
    print("Первое письмо: " + goodmail)

    f1 = email_features(process_email(goodmail))
    pr = sum(f1 > 0)
    print('\nКоличество ненулевых элементов: %f' % pr)
    p = model.predict(f1.reshape(-1, 1899))
    res = np.mean(p == f1) * 100
    print('Результат: %f' % res)
    with open('badmail.txt', 'r') as file:
        badmail = file.read().replace('\n', '')
    print("\n\nВторое письмо: " + badmail)

    f2 = email_features(process_email(badmail))
    pr = sum(f2 > 0)
    print('\nКоличество ненулевых элементов: %f' % pr)
    p = model.predict(f2.reshape(-1, 1899))
    res = (p == f2).mean() * 100
    print('Результат: %f' % res)

if __name__ == '__main__':
    main()