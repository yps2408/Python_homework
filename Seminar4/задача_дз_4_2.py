# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N: '))
list = []
a = n
if n > 1:
    restart = True
    while restart:
        restart = False
        for i in range (2, n+1):
            if n%i == 0:
                list.append(i)
                n = int(n/i)
                restart = True
                break

    print(f'Простые множители числа {a} - {list}')
elif n == 1:
    print(f'Простые множители числа {a} - [1]')
else:
    print(f'Вы ввели не правильное число')