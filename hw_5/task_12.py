from random import randrange
english_text = "In all his posture there was no fear, not even alertness. This squirrel was very curious and trusting. After all, little squirrels do not understand where danger may lurk, they do not yet know their enemies. They are interested in everything in this vast world."

def calc(text, m):
    print(f'Числа, кратными заданному числу {m}:')
    words = text.replace('.', '').replace(',', '') \
        .replace(':', '').replace(';', '') \
        .replace('?', '').replace('!', '').replace('(', '').replace(')', '').split()
    for word in words:
        if word.isnumeric():
            if int(word) % m == 0:
                print(word)



m = int(input('Введите число: '))
arr = " ".join([str(randrange(10, 100)) for i in range(15)])
text_with_numbers = english_text + arr
print(f"Текст: {text_with_numbers}")
print("-----------------------------------------------------")
calc(text_with_numbers, m)