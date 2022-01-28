def enter_num() -> float:
    symbol = input("Введите символ: ")

    return check_input(symbol)


def check_input(symbol):
    if symbol.isnumeric():
        print(f'{symbol} - это цифра')
    elif symbol.isalpha():
        print(f'{symbol} - это буква')
    else:
        print(f'{symbol} - это спец знак')

    print(f"Ответ равен: {symbol}")

    return True


enter_num()
