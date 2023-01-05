# for i in range(1, 6, 3):
#     print(i)
# from typing import List, Any

# count = 0
# word = "Hello word!"
# for i in word:
#     if i == "l":
#         count += 1
#
# print("Count:", count)

# isHascar = True
#
# while isHascar:
#     if input("Enter data: ") == "Stop":
#         isHascar = False

# for i in range(1, 11):
#     if i == 5:
#         break
#
#     if i % 2 == 0:
#         continue
#
#     print(i)
# found = None
# for i in "hello":
#     if i == "m":
#         found = True
#         break
# else:
#     found = False
#
# print(found)
# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1
# import numexpr
# from colorama import init
# from colorama import Fore, Back, Style
#
# init()
#
# print(Fore.BLUE)
#
# expr = input('Введите математическую выражение: ')
#
# result = numexpr.evaluate(expr)
#
# print(Fore.LIGHTYELLOW_EX)
# print(f'Результат: {result}')
# a = float(int(input('Введите первое число: ')))
# b = float(int(input('Введите второе число: ')))
#
# print(Fore.GREEN)
# operation = input('что сделать? (+, -, *, /): ')
# result = 0
#
# if operation == '+':
#     result = a + b
# elif operation == '-':
#     result = a - b
# elif operation == '*':
#     result = a * b
# elif operation == '/':
#     result = a / b
# else:
#     print('eror')

# import python_weather
# import asyncio
# import os
#
#
# async def getweather():
#     # declare the client. format defaults to the metric system (celcius, km/h, etc.)
#     async with python_weather.Client(format=python_weather.IMPERIAL) as client:
#
#         # fetch a weather forecast from a city
#         weather = await client.get("New York")
#
#         # returns the current day's forecast temperature (int)
#         print(weather.current.temperature)
#
#         # get the weather forecast for a few days
#         for forecast in weather.forecasts:
#             print(forecast.date, forecast.astronomy)
#
#             # hourly forecasts
#             for hourly in forecast.hourly:
#                 print(f' --> {hourly!r}')
#
#
# if __name__ == "__main__":
#     # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
#     # for more details
#     if os.name == "nt":
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
#     asyncio.run(getweather())

# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# clean_string = ""
# for letter in letters:
#     if not letter.isupper():
#         clean_string += letter
#     letters = clean_string
#     print(letters)

# rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for position in range(11):
#     print('^' * 27)
#     for letter in rus_lower:
#         if rus_lower.index(letter) % 11 == position:
#             print('| ', letter.upper(), letter, ' |', end='')
#     print()
# print('^' * 27)

# nick = input("What's your name?")
# secret_list = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']
#
# while nick not in secret_list:
#     print('Тут ничего нет. Еще есть вопросы?')
#     nick = input()
# else:
#     print(f'Ты – свой. Приветствую, любезный {nick}!')

# lst = [32, True, 'python', 2.35]
# lst.reverse()
# print(lst)
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# lst_test = [32, True, 'python', 2.35]
# print(change(lst_test))

# def to_list(*args):
#     return list(args)
#
#
# print(to_list(1, 5, 77))

# def useless(lst):
#     big = max(lst)                                  # return max(lst) / len(lst)
#     middle = big / len(lst)                         # можно было сократить код таким образом
#     middle = round(middle, 2)
#     return middle
#
#
# lst_test = [32, 55, 98, 235, 90, 87, 77]
# print(useless(lst_test))

# def list_sort(lst):
#     lst.sort(reverse=True)
#     return lst
#
#
# lst_test = [32, 55, 98, 235, 90, 87, 77]
# print(list_sort(lst_test))

# def all_eq(lst):
#     max_item = max(lst, key=lambda x: len(x))
#     max_len = len(max_item)
#     return [item.ljust(max_len, '_') for item in lst]
#
#
# lst_test = ['крот', 'белка', 'выхухоль']
# print(all_eq(lst_test))

# def tpl_sort(tpl):
#     for element in tpl:
#         if not isinstance(element, int):
#             return tpl
#     return tuple(sorted(tpl))
#
#
# tpl_test = (22, 32, 1, 12)
# print(tpl_sort(tpl_test))

# def sieve(lst):
#     lst = tuple(lst)
#     return lst[::-1]
#
#
# lst_test = [2, 55, 1, 1]
# print(sieve(lst_test))
