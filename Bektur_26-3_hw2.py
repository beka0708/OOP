while True:
    input('С помощью этой программы вы узнаете свой знак зодиака (нажмите "Enter" чтобы продолжить) ')
    birthday = int(input('Введите день рождения: '))
    month = int(input('Введите месяц рождения: '))
    if 21 <= birthday <= 31 and month == 3 or birthday >= 1 and birthday <= 20 and month == 4:
        print('Ваш знак зодиака "Овен"')
    elif 21 <= birthday <= 30 and month == 4 or birthday >= 1 and birthday <= 21 and month == 5:
        print('Ваш знак зодиака "Телец"')
    elif 22 <= birthday <= 31 and month == 5 or birthday >= 1 and birthday <= 21 and month == 6:
        print('Ваш знак зодиака "Близнецы"')
    elif 22 <= birthday <= 30 and month == 6 or birthday >= 1 and birthday <= 22 and month == 7:
        print('Ваш знак зодиака "Рак"')
    elif 23 <= birthday <= 31 and month == 7 or birthday >= 1 and birthday <= 21 and month == 8:
        print('Ваш знак зодиака "Лев"')
    elif 22 <= birthday <= 31 and month == 8 or birthday >= 1 and birthday <= 23 and month == 9:
        print('Ваш знак зодиака "Дева"')
    elif 24 <= birthday <= 30 and month == 9 or birthday >= 1 and birthday <= 23 and month == 10:
        print('Ваш знак зодиака "Весы"')
    elif 24 <= birthday <= 31 and month == 10 or birthday >= 1 and birthday <= 22 and month == 11:
        print('Ваш знак зодиака "Скорпион"')
    elif 23 <= birthday <= 30 and month == 11 or birthday >= 1 and birthday <= 22 and month == 12:
        print('Ваш знак зодиака "Стрелец"')
    elif 23 <= birthday <= 31 and month == 12 or birthday >= 1 and birthday <= 20 and month == 1:
        print('Ваш знак зодиака "Козерог"')
    elif 21 <= birthday <= 31 and month == 1 or birthday >= 1 and birthday <= 19 and month == 2:
        print('Ваш знак зодиака "Водолей"')
    elif 20 <= birthday <= 28 and month == 2 or birthday >= 1 and birthday <= 20 and month == 3:
        print('Ваш знак зодиака "Рыбы"')
    else:
        print('ОШИБКА!!! \n'
              'Введите правильно дату')
