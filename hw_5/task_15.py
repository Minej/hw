rus_text = "Во всей его позе не было ни страха, ни даже насто­роженности. Этот бельчонок был очень любопытен и до­верчив. Ведь маленькие бель­чата не понимают, где может таиться опасность, не знают ещё   своих   врагов.   Им   всё интересно   в   этом огромном мире. \ntest текст стоп тут rs043"

def calc(text):
    count = 0
    changed_text = ""
    for index in range(0, len(text)):
        if text[index].isalpha() or text[index].isnumeric():
            if index != len(text) - 1:
                count += 1
                continue
            else:
                if text[index - count] != text[index]:
                    changed_text += ''.join(text[index - count:index + 1]) + " "
                    changed_text += ''.join(text[index - count:index + 1])
                    continue
        if count == 0:
            changed_text += text[index]
            continue
        if text[index - count] != text[index - 1]:
            changed_text += ''.join(text[index - count:index]) + " "
            changed_text += ''.join(text[index - count:index + 1])
        count = 0
    print(f"Текст после изменений: \n{changed_text}")
    words_count = len(changed_text.split())
    print(f"\nЧисло слов в тексте: {words_count}")




print(f"Текст: {rus_text}")
print("-----------------------------------------------------")
calc(rus_text)