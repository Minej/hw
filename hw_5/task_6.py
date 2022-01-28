english_text = "In all his posture there was no fear, not even alertness. This squirrel was very curious and trusting. After all, little squirrels do not understand where danger may lurk, they do not yet know their enemies. They are interested in everything in this vast world."


def calc(text):
    count_words = len(text.split())
    is_even = True if count_words % 2 == 0 else False
    changed_word = ""
    special_sign = ""
    changed_text = []
    for index in range(len(text) - 1, 1, -1):
        if text[index] == '.' or text[index] == ',' or text[index] == ':' or text[index] == ';' or \
                text[index] == '?' or text[index] == '!' or text[index] == '(' or text[index] == ')':
            special_sign = text[index]
            continue
        if text[index] == " ":
            changed_word += special_sign
            special_sign = ""
        if is_even:
            changed_word += text[index]
        if text[index] == " ":
            changed_text.append(changed_word)
            changed_word = ""
            is_even = False if is_even else True
    final_text = list(reversed(changed_text))
    print("".join(final_text))



print(f"Текст: {english_text}")
print("-----------------------------------------------------")
calc(english_text)