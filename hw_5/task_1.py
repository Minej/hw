def enter_num() -> float:
    l = ["лиственница", "привет", "как дела?", "мошенник"]

    return calc(l)


def calc(l):
    if "нн" in l:
        print("в слове есть удвоенное буквы н и это: ", l)
    else:
        print("в слове нет удвоенной буквы н")
        
    print("Короткое слова это: ", min((word for word in l if word), key=len))
    print("Длинное слова это: ",max((word for word in l if word), key=len))

    return True

enter_num()
