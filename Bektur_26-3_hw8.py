x = 0
y = 100
middle = 50
count = 0

with open('results.txt', 'w', encoding='UTF-8') as file:
    while True:
        print(f"Загаданное вами число равно {middle}?")
        file.write(f'{middle},')
        answer = input()
        count += 1
        if answer == '>':
            x = middle
            middle = (x + y) // 2
        elif answer == '<':
            y = middle
            middle = (x + y) // 2
        elif answer.lower() == 'да':
            file.write(f"\nКоличество попыток: {count}")
            file.write(f"\nЗагаданное число: {middle}")
            print('Ваши подробные результаты в файле "results"')
            break
        else:
            print('Неправильный ввод. Вводите да,< или >')
