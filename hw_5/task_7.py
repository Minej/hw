english_text = "In all his posture there was no fear, not even alertness. This squirrel was very curious and trusting. After all, little squirrels do not understand where danger may lurk, they do not yet know their enemies. They are interested in everything in this vast world."


def task_seven(text_seven):
    words = text_seven.replace('.', '').replace(',', '') \
        .replace(':', '').replace(';', '') \
        .replace('?', '').replace('!', '').replace('(', '').replace(')', '').split()
    last_word = words[len(words) - 1]

    for word in words:
        changed_word = ""
        if word == last_word:
            continue
        for char in word:
            if char not in changed_word:
                changed_word += char
        if len(word) > 2 and len(word) % 2 == 1:
            middle_index = int(len(word) / 2)
            changed_word = changed_word.replace(word[middle_index], '')
        print(f"Изначальное слово: '{word}'. Слово после преобразования: '{changed_word}'")



print(f"Текст: {english_text}")
print("-----------------------------------------------------")
task_seven(english_text)
