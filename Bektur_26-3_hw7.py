ten = list(range(1, 11))

evens = list(filter(lambda x: x % 2 == 0, ten))

square_evens = list(map(lambda x: x ** 2, evens))

# print(ten)
# print(evens)
# print(square_evens)
# def function(lst=(list(ten))):
while True:
    try:
        print('Чтобы выйти из программы напишите: Exit')
        index_user = input('Введите индекс: ')
        if str(index_user) == 'Exit':
            print('Вы завершили программу :)')
            break
        print(ten[int(index_user)])
    except IndexError:
        print(f'Только целые цифры, от 0 до {len(ten[:-1])}')
    except ValueError:
        print('Только цифры,Без букв!!')
