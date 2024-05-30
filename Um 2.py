user_number = int(input("Введите число: "))

negative_sum = 0
positive_sum = 0

for i in range(-user_number, user_number + 1):
    if i < 0:
        negative_sum += i
    else:
        positive_sum += i

print(f"Сумма отрицательных чисел: {negative_sum}")
print(f"Сумма положительных чисел: {positive_sum}")
