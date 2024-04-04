# # ввод целого числа
# d1, d2, d3, d4, d5 = map(int, input().split())
#
# # здесь продолжите программу
# print(min(d1, d2, d3, d4, d5))

# import math

# a, b = map(int, input().split())
# print(round(math.sqrt(a**2+b**2),2))

# n, k = map(int, input().split())
# c = int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
# print(c)

# x = int(input())
# price = x - x * 0.1
# print(math.floor(500/price))

# n = int(str(float(input())).split(".")[1][:2])
# print(n > 50)

# a, b = map(int, input().split())
# print(a % b == 0)

# a, b, c = map(int, input().split())
# print(a + b > c and a + c > b and b + c > a)

# n = float(input())
# print(0 <= n <= 2 or 10 <= n <= 20)

# t1 = input()
# t2 = input()
# print(t1, t2)

# print((1+2)*('7'+'8'))

# a, b = map(str, input().split())
# print(a, a, b, b, b)

# a, b = map(int, input().split())
# print("Переменная a = " + str(a) + ", переменная b = " + str(b))

# s = input()
# print("Строка: "+s+". Длина: "+str(len(s)))

# a, b = map(str, input().split())
# print(a in b, a == b, a > b, a < b)

# char1, char2 = map(str, input().split())
# print(f'Коды: {char1} = {str(ord(char1))}, {char2} = {str(ord(char2))}')

# s = input()
# print(s[:1]+s[-1:])

# s1 = input()
# s2 = input()
# print(s1[0::2], s2[1::2])

# s1, s2 = map(str, input().split())
# print(s1[1:len(s2):2] == s2[1::2])

# a, b, c = map(int, input().split())
# print(f'{str(a // 100)}{str(a % 100 // 10)}{str(a % 10)}\n{str(b // 100)}{str(b % 100 // 10)}{str(b % 10)}\n{str(c // 100)}{str(c % 100 // 10)}{str(c % 10)}')

# a, b, c = map(str, input().split())
# a = a.rjust(3, '0')
# b = b.rjust(3, '0')
# c = c.rjust(3, '0')
# print(a + '\n' + b + '\n' + c)

name = input()
lastName = input()
age = int(input())
print('Уважаемый {name} {lastName}! Поздравляем Вас с {age}-летием!'.format(name=name, lastName=lastName, age=age))


print('test github')