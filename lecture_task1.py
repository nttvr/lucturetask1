# Задача на For:
# 1.
# На вход программе подается натуральное число 𝑛. Напишите программу, которая выводит звездный треугольник в соответствии с примером.
#
# n = 3
#
# ***
# **
# *
# РЕШЕНИЕ:

n = int(input('Введите число: '))
for i in range(n):
    print('*' * n)
    n -= 1

# 2.
# Напишите программу, на вход которой даются четыре числа a, b, c и d
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [𝑎;𝑏] на все числа отрезка [𝑐;𝑑].
# Числа 𝑎, b, c и 𝑑 являются натуральными и не превосходят 10, 𝑎≤𝑏, 𝑐≤𝑑.
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.
#
# a,b,c,d = 7,10,5,6
#
#     5     6
# 7  35  42
# 8  40  48
# 9  45  54
# 10  50  60
# РЕШЕНИЕ:

a, b, c, d = map(int, input('Введите числа: ').split())
if (a, b, c, d < 10) and (a <= b) and (c <= d):
    for i in range(c, d + 1):
        print(end='\t' + str(i))
    print('')
    for j in range(a, b + 1):
        print(j, end='')
        for k in range(c, d + 1):
            print(end='\t' + str(k * j))
        print('')

# 3.
# Дано натуральное число 𝑛. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:
#
# n =  6
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# РЕШЕНИЕ

n = int(input('Введите число: '))
count = 1
count2 = n
for i in range(n):
    count2 -= 1
    for j in range(n - count2):
        print(count, end=' ')
        count += 1
    print('')

# Задачи на If:
# 1.
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).
#
# a,b,c = 59, 59, 59
# result —> Равносторонний
# РЕШЕНИЕ

a, b, c = map(int, input('Введите длины сторон треугольника: ').split())
if ((a, b, c > 0) and (a + b + c == 180)):
    if (a == b == c):
        print('Треугольник равносторонний!')
    elif ((a != b != c) and (a != c)):
        print('Треугольник разносторонний!')
    else:
        print('Треугольник равнобедренный!')
else:
    print('Ошибка! Проверьте, чтобы введеные числа были > 0 и в сумме давали 180 градусов')

# 2.
# На вход программы подается 3 целых числа. Напишите программу, которая находит серединное значение из этих чисел
#
# a,b,c = 67, 100, 54
# result —> 67
# РЕШЕНИЕ

a, b, c = map(int, input('Введите три числа: ').split())
if (a < b and a > c) or (a > b and a < c):
    print(a)
elif (b < a and b > c) or (b > a and b < c):
    print(b)
elif (c < a and c > b) or (c > a and c < b):
    print(c)
else:
    print('Введите разные числа!')

# 3.
# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#
#  -если смешать красный и синий, то получится фиолетовый;
#  -если смешать красный и желтый, то получится оранжевый;
#  -если смешать синий и желтый, то получится зеленый.
#
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.
#
# a,b = красный, синий
# result —> фиолетовый
# РЕШЕНИЕ

color1, color2 = input('Введите 2 цвета: "красный", "синий" или "желтый": ').split()
if (color1.lower() == 'красный' and color2.lower() == 'синий') or (
        color2.lower() == 'красный' and color1.lower() == 'синий'):
    print('Получается фиолетовый!')
elif ((color1.lower() == 'красный' and (color2.lower() == 'желтый' or color2.lower() == 'жёлтый')) or (
        color2.lower() == 'красный' and (color2.lower() == 'желтый' or color2.lower() == 'жёлтый'))):
    print('Получается оранжевый!')
elif ((color1.lower() == 'синий' and (color2.lower() == 'желтый' or color2.lower() == 'жёлтый')) or (
        color2.lower() == 'синий' and (color2.lower() == 'желтый' or color2.lower() == 'жёлтый'))):
    print('Получается зеленый!')
else:
    print('Ошибка!')
