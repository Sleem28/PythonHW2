# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    
#     *Пример:*
    
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_list(number: int) -> list:
    list       = []
    tmp        = 1
    multiplier = 2
    
    list.append(tmp)

    for item in range(1,number):
        tmp *= multiplier
        list.append(tmp)
        multiplier += 1
    
    return list

print(get_list(int(input('Введите целое число: '))))