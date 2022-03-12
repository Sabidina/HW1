# задание 1
a = input('Введите переменую: ')
a = int(a)
b = 12
total = (a+b)
print('Сумма: ', total)
name = input('Как вас зовут?')
print('Привет, ', name)

# задание 2
time = input('Введите ваше время в сек.: ')
time = int(time)
hours = time // 3600
print('Итого: ',hours, 'часов')
min = (time - hours * 3600) // 60
print('Итого: ',min, 'минут')
sec = time - (hours * 3600 + min * 60) // 60
print('Получаем в формате чч:мм:сс : ',hours,min,sec,sep=':')

# задание 3
n = input('Введите целое число "n" от 1 до 9: ')
nn = str(n*2)
nnn = str(n*3)
total = int(n) + int(nn) + int(nnn)
print('Сумма: ', n, '+', nn,'+',nnn,'=', total)

# задание 4
n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальня цифра в числе: ", max)
        break

# задание 5
p = input('Укажите значение выручки вашей компании: ')
i = input('Укажите значение издержек вашей компании: ')
p = int(p)
i = int(i)
total = int(p-i)
print('Финансовый результат вашей фирмы = ',total)
if p>i:
    print('Ваша компания в прибыли!Поздравляем!')
else:
    print('Вы в убытке.')

 # задание 6
if p>i:
    prib = p-i
    rent = float(prib%i)
    print('Рентабельность выручки:',rent)
n = input('Укажите численность сотрудников вашей компании: ')
sotr = prib%1
print('Прибыль фирмы в расчёте на одного сотрудника = ', prib)
