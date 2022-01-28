rus_text = "Во всей его позе не было ни страха, ни даже насто­роженности. Этот бельчонок был очень любопытен и до­верчив. Ведь маленькие бель­чата не понимают, где может таиться опасность, не знают ещё   своих   врагов.   Им   всё интересно   в   этом огромном мире."
english_text = "In all his posture there was no fear, not even alertness. This squirrel was very curious and trusting. After all, little squirrels do not understand where danger may lurk, they do not yet know their enemies. They are interested in everything in this vast world."


def task_sixteen(text_sixteen_one, text_sixteen_two, n_one, n_two):
    changed_text = text_sixteen_one[0:n_one]
    changed_text += text_sixteen_two[len(text_sixteen_two) - n_two:len(text_sixteen_two)]
    print(f"\nНовая строка: {changed_text}")



print(f"Текст s1: {rus_text}")
print("-----------------------------------------------------")
print(f"Текст s2: {english_text}")
print("-----------------------------------------------------")
n_one = abs(int(input('Введите число N1: ')))
n_two = abs(int(input('Введите число N2: ')))
task_sixteen(rus_text, english_text, n_one, n_two)