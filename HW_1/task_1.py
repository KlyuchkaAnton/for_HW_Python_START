# ////////////////////////////////////////////////////////////////////////////////////////////////////
# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# ////////////////////////////////////////////////////////////////////////////////////////////////////
# a=123//100
# b=123%10 
# v=123//10-10

# ------------1 метод--------------
# a=100//100
# b=100%10 
# v=100//10-10

# print(a)
# print(b)
# print(v)
# print(a+b+v)

# ------------2 метод--------------

# n = int(input())
# summa = 0
# while n > 0:
#     digit = n % 10
#     summa = summa + digit
#     n = n // 10
# print (summa)
# 
