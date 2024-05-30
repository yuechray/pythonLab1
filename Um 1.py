while True:
    user_input = input("Введите число или 'exit' для выхода: ")

    if user_input.lower() == 'exit':
        print("Выход из программы...")
        break

    if not user_input.isdigit():
        print("Ошибка: введено не число. Пожалуйста, введите число.")
        continue

    length = len(user_input)
    print(f"Длина введенного числа: {length}")
