rus_text = "Во всей его позе не было ни страха, ни даже насто­роженности. Этот бельчонок был очень любопытен и до­верчив. Ведь маленькие бель­чата не понимают, где может таиться опасность, не знают ещё   своих   врагов.   Им   всё интересно   в   этом огромном мире."


def calc(text_four):
    changed_text = ""
    count = 1
    for symbol in text_four:
        if not symbol.isalpha():
            count = 1
            changed_text += symbol
            continue
        if count % 2 == 0 and symbol == 'а':
            changed_text += 'е'
        elif count % 2 == 1 and symbol == 'б':
            changed_text += 'ак'
        else:
            changed_text += symbol
        count += 1
    print(changed_text)


print(f"Текст: {rus_text}")
print("-----------------------------------------------------")
calc(rus_text)