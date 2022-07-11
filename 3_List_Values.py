#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#----------------------------------------------------------------------------------------------------------------+
def get_value(number: int) -> float:
    res = (1 + 1/number)**number
    return res
#----------------------------------------------------------------------------------------------------------------+
def set_value_to_list(number: int) -> list:
    list =[]
    for i in range(1,number):
        list.append(get_value(i))
    
    return list
#----------------------------------------------------------------------------------------------------------------+
def get_list_sum(list: list) -> float:
    xsum = 0.0
    for item in list:
        xsum += item
    return xsum
#----------------------------------------------------------------------------------------------------------------+
def print_result(list: list):
    index = 1

    for item in list:
        print(f'Элемент с номером {index} равен {item}.')
        index += 1

    print(f'Сумма всех элементов последовательности равна {get_list_sum(list)}')
#----------------------------------------------------------------------------------------------------------------+
list = set_value_to_list(int(input('Введите число для расчета последовательности: ')))
print_result(list=list)