
ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
shot = input("Введите координаты выстрела: ")

if any(shot.lower() in position.lower()
       for position in ship.split()):
    print("Попадание!")
else:
    print("Мимо!")

# Задание №4.2
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

result = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age)
print(result)
