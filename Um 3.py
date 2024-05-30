import itertools

user_input = input("Введите трехзначное число с разными цифрами: ")

if not user_input.isdigit() or len(user_input) != 3 or len(set(user_input)) != 3:
    print("Ошибка: введите трехзначное число с разными цифрами.")
else:
    permutations = [int(''.join(p)) for p in itertools.permutations(user_input, 3)]
    for number in permutations:
        print(number)
