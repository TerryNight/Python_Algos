"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def fun(number, k=0, f=1):
    if k == f:
        print(f"{k == f}")

    elif k < f:
        return fun(number, k+1, number * (number + 1) // 2)


try:
    NUMBER = int(input("Введите число: "))
    fun(NUMBER)
except ValueError:
    print("Вы ввели некорректные данные")