same_words = []
words = []


def single_root_words(root_word, *other_words):
    same_words = []
    words = []
    word = str(root_word).lower()
    other_words = str(*other_words)
    l = 0
    start = 0
    while l < len(other_words):
        ltr = other_words[l]
        if ltr == ' ':
            l = l + 1
            nxt_word = other_words[start:l - 1]
            start = l
            if len(nxt_word) == 0:
                continue
            words.append(nxt_word)
            if nxt_word.lower() in word:
                print(f'{root_word} содержит слово {nxt_word}')
                same_words.append(nxt_word)
            elif word in nxt_word.lower():
                same_words.append(nxt_word)
        elif l == len(other_words) - 1:  # проверим последнее слово
            words.append(other_words[start:l + 1])
            if other_words[start:l + 1].lower() in word:
                print(f'{root_word} содержит слово {nxt_word}')
                same_words.append(other_words[start:l + 1])
            elif other_words[start:l + 1].lower().count(word):
                same_words.append(other_words[start:l + 1])
            break
        else:
            l = l + 1
            continue
    print('Проверяемые слова:', words)

    l_other_words = ' ' + other_words.lower() + ' '
    n = l_other_words.count(word)

    print("Проверочное слово: ", root_word)
    if n == 0:
        print('Однокоренных слов не встретилось')
    else:
        s = l_other_words.count(' ')
    return same_words


root_word = 'пЕч'
other_words = 'пЕченный пЕчка в пЕчи хлеб готовится'
print(type(other_words))

single_root_words(root_word, other_words)
print('Однокоренные слова:\n', *same_words)
print(' ' + '~' * len(other_words))

root_word = 'Брат'
other_words = 'Братишка Братец'
print(type(other_words))

single_root_words(root_word, other_words)
print('Однокоренные слова:\n', *same_words)
print(' ' + '~' * len(other_words))

print('Проверка')
root_word = str(input('Введите искомый корень: '))
other_words = str(input('Введите строку с остальными словами: '))
single_root_words(root_word, other_words)
