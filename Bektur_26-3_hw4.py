letters = []
numbers = []

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1, 2)
letters.reverse()
numbers.sort()
numbers = [i ** 2 for i in numbers]
letters[1] = "G"
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
