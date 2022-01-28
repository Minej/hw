rus_text = "Во всей его позе не было ни страха, ни даже насто­роженности. Этот бельчонок был очень любопытен и до­верчив. Ведь маленькие бель­чата не понимают, где может таиться опасность, не знают ещё   своих   врагов.   Им   всё интересно   в   этом огромном мире."


def calc(text):
    words = text.replace('.', '').replace(',', '') \
        .replace(':', '').replace(';', '') \
        .replace('?', '').replace('!', '').replace('(', '').replace(')', '').split()
    print(f'Количество слов в данной строке: {len(words)}')
    last_word = words[len(words) - 1]
    count_a = last_word.count('а')
    print(f'Количество букв "а" в последнем слове "{last_word}": {count_a}')
    words_starts_b = len([word for word in words if word.startswith('б')])
    print(f"Количество слов, начинающихся с буквы 'б': {words_starts_b}")
    words_same_start_end = len([word for word in words if word[0] == word[len(word) - 1]])
    print(f"Количество слов, у которых первый и последний символы совпадают между собой "
          f"(включая слова из одной буквы): {words_same_start_end}")



print(f"Текст: {rus_text}")
print("-----------------------------------------------------")
calc(rus_text)