import numpy as np
from porterStemmer import porterStemmer
import re

def get_dictionary():
  with open('dictionary.txt') as f:
    dictionary = []
    for line in f:
      idx, w = line.split()
      dictionary.append(w)
  return np.array(dictionary)

def process_email(email):
  vocabList = get_dictionary()
  word_indices = []

  # приведение текста к нижнему регистру
  email = email.lower()

  # удаление html-тегов из текста письма
  rx = re.compile('<[^<>]+>|\n')
  email = rx.sub(' ', email)

  # числа заменяются на строку 'number'
  rx = re.compile('[0-9]+')
  email = rx.sub('number ', email)

  # ссылки заменяются на строку 'httpaddr'
  rx = re.compile('(http|https)://[^\s]*')
  email = rx.sub('httpaddr ', email)

  # электронные адреса заменяются на строку 'emailaddr'
  rx = re.compile('[^\s]+@[^\s]+')
  email = rx.sub('emailaddr ', email)

  # значок $ заменяется на строку 'dollar'
  rx = re.compile('[$]+')
  email = rx.sub('dollar ', email)

  # удаление не буквенно-цифровых символов
  rx = re.compile('[^a-zA-Z0-9 ]')
  email = rx.sub('', email).split()

  for str in email:
    # приведене каждого слова к существительному в единственном числе 
    try:
      str = porterStemmer(str.strip())
    except:
      str = ''
      continue

    if len(str) < 1:
      continue

    # TODO: необходимо в word_indices добавить индекс слова str из словаря vocabList.
    # Чтобы узнать индекс слова в словаре, воспользуйтесь функцией where из библиотеки NumPy.
    # Функция принимает условие, возвращает пару значений как кортеж:
    #
    ans = np.where(vocabList == str)
    #
    # Первый элемент в кортеже представляет собой массив индексов словаря, где встретилось слово str.
    # Обратите внимание, что слово может отсутствовать в словаре. В этом случание в word_indices
    # ничего добавлять не нужно.
    # Для добавления элемента в Python-массив используется метод append:
    #
    # a = [1, 2, 3]
    # a.append(4)   # => [1, 2, 3, 4]
    mas = ans[0]
    for a in range(len(mas)):
      word_indices.append(mas[a])

  return word_indices

def email_features(word_indices):
  n = 1899  # общее число слов в словаре
  x = np.zeros(n)

  # TODO: необходимо установить в 1 элементы массива x,
  # соответствующие индексам из массива word_indices.
  # Данную операцию можно реализовать одной строкой кода
  # (см. способы индексации массивов в методичках по предыдущим практикам и лабораторным)
  for i in range(len(word_indices)):
    x[word_indices[i]] = 1

  return x
