english_text = "In all his posture there was no fear, not even alertness. This squirrel was very curious and trusting. After all, little squirrels do not understand where danger may lurk, they do not yet know their enemies. They are interested in everything in this vast world.Fjjjj t...ssest"


def calc(text):
    new_text = ""
    is_remove = False
    count_letters = dict()
    for index in range(0, len(text) - 1):
        if text[index] != text[index + 1]:
            if not is_remove:
                new_text += text[index]
            else:
                is_remove = False
        else:
            is_remove = True
    if not is_remove:
        new_text += text[len(text) - 1]

    for index in range(0, len(new_text)):
        if new_text[index] not in count_letters:
            count_letters[new_text[index]] = 1
        else:
            count_letters[new_text[index]] += 1
    print(new_text)
    print('Результат:')
    for key, value in count_letters.items():
        print(f"|| {repr(key)} || повторяется {value} раз(-а). ||")



text_thirteen = english_text
print(f"Текст: {text_thirteen}")
print("-----------------------------------------------------")
calc(text_thirteen)