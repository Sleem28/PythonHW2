# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

import random
#-----------------------------------------------------------------------------------------------------------------+
def fill_list(number: int) -> list:
    list = []
    for item in range(number):
        list.append(random.randint(-number,number))
    return list
#-----------------------------------------------------------------------------------------------------------------+
def mult_elements(list: list, text: str) -> str:
    list_elements = text.split(' ')
    
    num_list = int(list_elements[0])-1
    result = list[num_list]

    for item in range(1,len(list_elements)):
        num_list = int(list_elements[item])-1
        result *= list[num_list]
    
    return (f'Произведение элементов списка по номерам (не по индексам!!!) {list_elements} равно {result}.')
#-----------------------------------------------------------------------------------------------------------------+

number = int(input('Введите целое число: '))
list   = fill_list(number=number)
text   = input(f'Введите через пробел номера элементов, которые вы хотите перемножить: от 1 до {number}: ')
print()
print(f'Сгенерированный список имеет вид {list}. \n')
print(mult_elements(list=list, text=text))