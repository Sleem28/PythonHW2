# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    
#     *Пример:*
    
#     - 6782 -> 23
#     - 0,56 -> 11

def sum_digits (num: float) -> int:
    s_num = str(num)
    sum   = 0

    for item in s_num:
        if item != '.':
            sum += int(item)
    return sum


f_num = float(input('Введите вещественное число: '))
print(sum_digits(f_num))