def find_middle(word):
    length = len(word)

    # Если длина слова четная
    if length % 2 == 0:
        middle1 = length // 2 - 1
        middle2 = length // 2
        print(word[middle1] + word[middle2])
    # Если длина слова нечетная
    else:
        middle = length // 2
        print(word[middle])

# Примеры использования
word1 = 'test'
find_middle(word1)  # Результат: es

word2 = 'testing'
find_middle(word2)  # Результат: t