english_text = "In all his posture there was no fear, not even alertness. This squirrel was very curious and trusting. After all, little squirrels do not understand where danger may lurk, they do not yet know their enemies. They are interested in everything in this vast world."

def calc(text):
    words = text.replace('.', '').replace(',', '') \
        .replace(':', '').replace(';', '') \
        .replace('?', '').replace('!', '').replace('(', '').replace(')', '').split()
    last_word = words[len(words) - 1]
    for word in words:
        if word == last_word:
            continue
        if len(word) > 1:
            last_index = len(word) - 1
            first_letter = word[0]
            last_letter = word[last_index]
            changed_word = last_letter + word[1:last_index] + first_letter
        else:
            changed_word = word
        print(f"Изначальное слово: '{word}'. Слово после преобразования: '{changed_word}'")


print(f"Текст: {english_text}")
print("-----------------------------------------------------")
calc(english_text)