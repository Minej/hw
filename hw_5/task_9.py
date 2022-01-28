def myfunc(mstr):
    res = (''.join(char for n, char in enumerate(
        mstr) if not (char == 'о' and n % 2 == 0)))
    print(res)

if __name__ == '__main__':
    myfunc(mstr='Пейте дети молоко, будете здоровы')
