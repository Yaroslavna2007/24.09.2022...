# задание 1
#Дано действительное положительное число a и целоe число n.
#Вычисли a в степени n. Решение оформите в виде функции power(a, n).
#Стандартной функцией возведения в степень пользоваться нельзя. ЭТО ОЧЕНЬ ВАЖНОЕ УСЛОВИЕ
a = float(input())
n = int(input())
def power(a, n):
    for s in range(abs(n)):
        a = a * a
    if n >= 0 :
        return a
    else:
        a = 1/a
        return a
print(power(a, n))
