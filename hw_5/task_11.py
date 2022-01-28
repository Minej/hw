rus_text = "Во всей его позе не было ни страха, ни даже насто­роженности. Этот бельчонок был очень любопытен и до­верчив. Ведь маленькие бель­чата не понимают, где может таиться опасность, не знают ещё   своих   врагов.   Им   всё интересно   в   этом огромном мире."


def calc(text):
    words = text.replace('.', '').replace(',', '') \
        .replace(':', '').replace(';', '') \
        .replace('?', '').replace('!', '').replace('(', '').replace(')', '').split()
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы']
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'щ',
                  'ъ', 'ь']
    print("Слова, где количество гласных букв равно согласным:")
    for word in words:
        if word.isascii():
            continue
        lower_word = word.lower()
        count_vowel = sum([lower_word.count(vowel) for vowel in vowels])
        count_consonant = sum([lower_word.count(consonant) for consonant in consonants])
        if count_vowel == count_consonant:
            print(word)
    print(f"Длина самого короткого слова: {len(min(words, key=len))}")


print(f"Текст: {rus_text}")
print("-----------------------------------------------------")
calc(rus_text)
