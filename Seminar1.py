# 1 Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = int(input("Введите N "))

def degree_func(N):
    i=0
    while i!=N:
        exit=(-3)**i
    print(exit)
    
    

# 2 Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1. 
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def generate_number(n):
    number = {}
    for i in range(1,n+1):
        number[i] = 3*i+1
    return number

n = int(input("введите количество элементов "))
random=generate_number(n)
print(random)

# 3 Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

str1=input("Введите 1 строку => ")
str2=input("Введите 2 строку => ")
str_enter=str1.count(str2)

print(f"СТрока '{str2} входит в строку {str1}' {str_enter} Раз")

# 4 Подсчитать сумму цифр в вещественном числе.

float_number = input("Введите вещественное чило => ")

sum = 0
for i in float_number:
        if i !="." and i !="," and i !="-":
            sum += int(i)

print (f"Сумма цифр числа {float_number} ={sum}")


# 5 Написать программу получающую набор 
# произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def factorial(n):
    list = []
    num = 1
    for i in range(1,n+1):
        num*=i
        list.append(num)

    return list

collection = factorial(5)
print(collection)