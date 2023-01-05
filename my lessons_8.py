# file = open('file.txt', 'w', encoding='utf-8')
# # file.write('Бишкек, Кыргызстан')
# # file.close()
# #
# # with open('file.txt', 'a', encoding='utf-8') as file:
# #     file.write('222222')

with open('file.txt', 'r', encoding='utf-8') as file:
    print(file.read())
