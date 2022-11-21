digits = input("Введите последовательность чисел через пробел: ")
digits_replace = digits.replace(" ", "")

while digits_replace.isdigit() is False:
    print("Вы ввели неверные данные!")
    digits = input("Повторите ввод.\nВведите последовательность чисел через пробел: ")
    digits_replace = digits.replace(" ", "")

boss_digit = input("Введите число: ")

while boss_digit.isdigit() is False:
    print("Вы ввели неверные данные!")
    boss_digit = input("Повторите ввод.\nВведите число:")


digits_list_old = (list(map(int, digits.split())))
digits = digits + " " + boss_digit
digits_list = (list(map(int, digits.split())))
boss_digit = int(boss_digit)


def sorted(digits_list):
    for i in range(len(digits_list)):
        for j in range(len(digits_list)-i-1):
            if digits_list[j] > digits_list[j+1]:
                digits_list[j], digits_list[j+1] = digits_list[j+1], digits_list[j]

sorted(digits_list)

def binary_search_min(digits_list, boss_digit, left, right):
    if boss_digit < min(digits_list_old):
        return "Такого элемента в последовательности нет!\nВы ввели число которое меньше любого элемента в последовательности."

    middle = (right + left) // 2  # находим середину
    if digits_list[middle] == boss_digit:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif boss_digit < digits_list[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search_min(digits_list, boss_digit, left, middle - 1)
    else:  # иначе в правой
        return binary_search_min(digits_list, boss_digit, middle + 1, right)


def binary_search_max(digits_list, boss_digit, left, right):
    if boss_digit > max(digits_list_old):
        return "Такого элемента в последовательности нет!\nВы ввели число которое больше любого элемента в последовательности."

    middle = (right + left) // 2  # находим середину
    if digits_list[middle] == boss_digit:  # если элемент в середине,
        return middle   # возвращаем этот индекс
    elif boss_digit >= digits_list[middle]:  # если элемент больше элемента в середине
        # рекурсивно ищем в правой половине
        return binary_search_max(digits_list, boss_digit, right, middle+1)
    else:  # иначе в правой
        return binary_search_max(digits_list, boss_digit, middle-1, left)

sorted(digits_list_old)

print("-------------------------------------------------------")

print("Номер позиции близжайшего элемента,\n"
      "который меньше введенного числа", boss_digit, ":\n[", binary_search_min(digits_list, boss_digit, 0, len(digits_list)), "]")

print("-------------------------------------------------------")

print("Номер позиции близжайшего элемента,\n"
      "который больше или равен введенному числу", boss_digit, ":\n[", binary_search_max(digits_list, boss_digit, 0, len(digits_list)), "]")

print("-------------------------------------------------------")

print("Отсортированный список чисел:\n", digits_list_old)