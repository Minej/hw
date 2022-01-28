english_text = "It is named after the Arabs, a term initially used to describe peoples living in the Arabian Peninsula bounded by eastern Egypt in the west, Mesopotamia in the east, and the Anti-Lebanon mountains and northern Syria in the north, as perceived by ancient Greek geographers. Test: ABBA, Arabic, Aaaarabic "


def calc(text):
    words = text.split()
    new_words = []
    for word in words:
        count_a = word.count('a')
        count_b = word.count('b')
        if count_a > count_b:
            word = word.replace('b', '')
        word = word.upper()
        new_words.append(word)
    changed_text = " ".join(new_words)
    print(changed_text)



text = english_text
print(f"Текст: {text}")
print("-----------------------------------------------------")
calc(text)
