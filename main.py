s = 0
k = 15
d = k - 10
k = 4 * d
s = k - 50
print (s)
#2
x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7
print(x)
#3 три последовательных числа
n = int(input())
print(' Первое число:',n,'\n','Второе число:',n+1,'\n','Третье число:',n+2,'\n')
#4 сумма трех чисел
n = int(input())
x = int(input())
t = int(input())
print(n+x+t)
#5 Площадь куба
n = int(input())
print('Площадь полной поверхности:',6*n**2,'\n','Объем:',n**3)
#6 Значение функции
a = int(input())
b = int(input())
print('3*(a+b)^3 + 275*b^2 - 127*a - 41 = ', 3*(a+b)**3 + 275*b**2 - 127*a -41)
#7 следующее и предыдущее
n = int(input())
print('Следущее за числом',n,'число: ',n+1)
print('Для числа',n,'предыдущее число: ',n-1)
#8 Стоимость покупки пк
n = int(input())
b = int(input())
c = int(input())
e = int(input())
print((n+b+c+e)*3)
#9 Арифметические операции
x = int(input())
y = int(input())
print(x+y,'сумма \n', x*y,'произведение \n',x-y, 'разность \n')
#10 Арифметическая прогрессия
y = int(input())
x = int(input())
n = int(input())
print(((2*n+(x-1)*y)*x/2))
#11 1 число x5
n = int(input())
print(n,'---',2*n,'---',3*n,'---',4*n,'---',5*n,)
#12 Геометрическая прогрессия
y = int(input())
x = int(input())
n = int(input())
print(y*x**(n-1))
#13 Расстояние в метрах
n = int(input())
print(n//100)
#14 Мандарины и школьники
n = int(input())
k = int(input())
print(k//n,'целое число мандарин\n',k%n,'в корзине')
#15 насееление разделить на 2 если чет или +1/2 если нечет
n = int(input())
if n % 2 != 0:
    print(n//2+1)
else:
    print(n//2)
#16 Номер купе 
n = int(input())
print(n//4+1)
#17 Разделение на часы и минуты
n = int(input())
hours = n//60
minut = n%60
print(hours,'часов',minut,'минут')
#18 Трехзначное число плюс и умножить
n = int(input('число'))
f = n//100
s = n//10%10
l = n%10
print(f+s+l,f*s*l)
#19 Перестановка
n = int(input())
f = n // 100
s = n // 10 % 10
l = n % 10
f = str(f)
s = str(s)
l = str(l)
print(f+s+l)
print(f+l+s)
print(s+f+l)
print(s+l+f)
print(l+f+s)
print(l+s+f)
#20 Деление цифр на тысячи сотни десятки и единицы
n = int(input())
print(n//1000,n%1000//100,n%100//10,n%10)
#21 пароль
n = input('password')
s = input('confirm password')
if n == s:
    print('Password is true')
else:
    print('Password is false')
#22 чет нечет
n = int(input())
if n % 2 !=0:
    print('Нечетное')
else:
    print('Четное')
#23 1+4 = 2-3
n = int(input())
a = n // 1000
b = n % 1000 // 100
c = n % 100 // 10
d = n % 10
if a+d == b-c:
    print('Да')
else:
    print('Нет')
#24 Возраст если больше 18 можно 
n = int(input('Возраст'))
if n >= 18:
    print('Можно')
else:
    print('Нельзя')
#25 Арифметическая прогрессия 3 числа
n = int(input())
b = int(input())
d = b-n
c = int(input())
if c == b + d:
    print('YES')
else:
    print('NO')
#26 Наименьшее из двух чисел
n = int(input())
b = int(input())
if n - b > 0:
    print(n)
else:
    print(b)
#27 Наименьшее из четырех чисел
n = int(input())
b = int(input())
c = int(input())
a = int(input())
if n - b > 0 and n - c > 0 and n - a >0:
    print(n)
elif b - c > 0 and b - a >0:
    print(b)
elif c - a > 0:
    print(c)
else:
    print(a)
#28 возрастная группа
n = int(input('Возраст'))
if n <= 13:
    print('Детство')
elif n>=14 and n<=24:
    print('Молодость')
elif n>=25 and n<=59:
    print('Зрелость')
else:
    print('Старость')
#29 считает только плюсы
sum = 0
i = 0
while i < 3:
    n = int(input())
    i = i+1
    if n>0:
        sum= sum+n
print(sum)
#30 число четырехзначное и делится на 7 или 17 без остатка = красивое
n = int(input())
if n//1000 !=0 and n%7 ==0 or n%17 ==0:
    print('Да')
else:
    print('Нет')
#31 может ли существовать треугольник с такими сторонами 
n = int(input())
b = int(input())
c = int(input())
if n + b > c and n+c>b and b+c > n:
    print('Да')
else:
    print('Нет')
#32 проверка года на високосность
n = int(input('Возраст'))
if n % 4 == 0 and n % 100 !=0:
    print('Да')
else:
    print('Нет')
#33 ход ладьи под 2 строки\столбца
f1 = int(input())
n1 = int(input())
f2 = int(input())
n2 = int(input())
if f1 == f2 or n1 == n2:
    print('Да')
else:
    print('Нет')
#34 король даны 2 столбца\строки
f1 = int(input())
n1 = int(input())
f2 = int(input())
n2 = int(input())
if (f1 == f2+1 or f1 == f2-1 or f1==f2) and (n1 == n2 or n1 == n2+1 or n1==n2-1):
    print('Да')
else:
    print('Нет')
#35 Калькулятор
a = int(input()) # Получите первое число 
b = int(input()) # Получите второе число
c = (input()) # получить операцию
if c == '+': # если операция + то выполнить:
    print(a+b) # написать значение a+b
elif c == '-': # если операция - то выполнить:
    print (a-b) # написать значение a-b
elif c == '*': # если операция * то выполнить:
    print(a*b) # написать a*b
elif c == '/': # если операция / то выполнить:
    if b != 0: # при b не равном нулю выполнить:
        print(a/b) # написать a/b
    else: # иначе выполнить:
        print('На 0 делить нельзя!') # На ноль делить нельзя
else: # в другом случае:
    print('Неверная операция!') # операция неверно указана
#36 сокрость зум и флеш
n = int(input()) # получаем значение скорости зума
k = int(input()) # получаем значение корости флеша
if n > k: # если скорость флеша больше нежели скорость зума то:
    print('зум быстрее') # написать зум быстрее
elif n < k: # если скорость флеша больше то:
    print('флеш быстрее') # написать флеш быстрее
else: # в другом случае выполнить:
    print('Не знаю') # написать "не знаю"
#37 вид треугольника
a = int(input()) # получаем первую сторону
b = int(input()) # получаем вторую сторону
c = int(input()) # получаем третью сторону
if (a == b and b != c and a != c) or (a == c and a != b and c != b) or (b == c and b != a and c != a): # если... или ... или... то выполнить:
    print('Равнобедренный') # написать равнобедренный
elif a == b and a == c and c == b: # если ... и ... и ... то выполнить:
    print('Равносторонний') # написать равносторонний
else: # в другом случае выполнить:
    print('Разносторонний') # написать разносторонний
#38 среднее число
a = int(input())
b = int(input())
c = int(input())
if (a > b and a < c) or (a > c and a < b):
    print(a)
elif (b > a and b < c) or (b > c and b < a):
    print(b)
else:
    print(c)
