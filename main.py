#  module_2_3
# Исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Начальный индекс
i = 0

while i < len(my_list):
    # Получаем текущее число
    current_number = my_list[i]

    if current_number == 0:
        # Если число равно нулю, продолжаем цикл без вывода
        i += 1
        continue

    if current_number > 0:
        # Выводим положительное число
        print(current_number)
        i += 1
    else:
        # Прерывание цикла при встрече первого отрицательного числа
        break



