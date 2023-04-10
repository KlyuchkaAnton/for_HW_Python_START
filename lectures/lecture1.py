# print('Введите первое число')  
# a = int(input())

# b = int(input('Введите второе число: '))

# print(a,'+',b,'=',a + b )

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# v = 'fvdfv'
# v = int (v)

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))
# # round(1.56566, 2)

# a = 1 > 4
# print (a)

# a = 1 < 4 and 5 > 2
# print (a)

# a = 1 == 2
# print (a)

# a = 1 != 2
# print (a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 3 < 10
# print (a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это Маша!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Эльнар':
#     print('Ильнар - топ')
# else:
#     print('Привет,', username)
    
# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожжалуй')
#     print('хватит )')
# print(i)


# минимальный делитель данного числа
# n = int (input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1
    
    
# a = 'qwerty'
# for i in a:
#     print (i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = "съEшь ещё этиХ Мягких французCких Булок"
# # print(len(text))
# # print('ещё' in text)
# # print(text.lower())
# # print(text.upper())
# print(text.replace('ещё', 'ЕЩЁЁЁЁЁ'))

# text = "съEшь ещё этиХ Мягких французCких Булок"

# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] #
# print(text)