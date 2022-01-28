english_text = "In all his posture there was no fear, not even alertness. This squirrel was very curious and trusting. After all, little squirrels do not understand where danger may lurk, they do not yet know their enemies. They are interested in everything in this vast world. test:ffffffffffffffffffff000000000004f0"


def calc(text):
    count_letters = dict()
    for index in range(0, len(text)):
        if text[index] not in count_letters:
            count_letters[text[index]] = 1
        else:
            count_letters[text[index]] += 1
    for key, value in count_letters.items():
        text = text.replace(key, '', value - 1)
    print(text)



print(f"Текст: {english_text}")
print("-----------------------------------------------------")
calc(english_text)