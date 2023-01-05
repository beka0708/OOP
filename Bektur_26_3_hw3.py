vowel_all = [
    "а", "о", "у", "ы", "э", "я", "е", "ё", "ю", "и", \
    "А", "О", "У", "Ы", "Э", "Я", "Е", "Ё", "Ю", "И", \
    "a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"
]
while True:
    print('Чтобы выйти из программы напишите: Exit')
    user = input('Введите слово: ')
    if user == 'Exit':
        print('Вы завершили программу :)')
        break
    elif user.isalpha():
        letter = 0
        vowel = 0
        consonant = 0
        for item in user:
            letter += 1
            if item in vowel_all:
                vowel += 1
            else:
                consonant += 1
    else:
        print("Введите одно слово!")
        break

    print(f'Ваше слово: {user}')
    print(f'Количество букв: {letter}')
    print(f'Количество гласных: {vowel}')
    print(f'Количество согласных: {consonant}')
    vowel = round(vowel / len(user) * 100, 2)
    print(f"Гласные/Согласные: {vowel} % / {round(100 - vowel, 2)} %")
