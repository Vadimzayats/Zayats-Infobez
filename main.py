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
f1 = int(input()) # получаем первую строку
n1 = int(input()) # получаем первый столбец
f2 = int(input()) # получаем строку после хода
n2 = int(input()) # получаем столбец после хода
if f1 == f2 or n1 == n2: # если строка не изменилась или не изменился столбец то выполнить:
    print('Да') # написать "Да"
else: # иначе
    print('Нет') # Написать "Нет"
#34 король даны 2 столбца\строки
f1 = int(input()) # получаем первую строку
n1 = int(input()) # получаем первый столбец
f2 = int(input()) # получаем строку после хода
n2 = int(input()) # получаем столбец после хода
if (f1 == f2+1 or f1 == f2-1 or f1==f2) and (n1 == n2 or n1 == n2+1 or n1==n2-1): # Если (... или ... или ...) и (... или ... или ...) то выполнить:
    print('Да') # Написать "Да"
else: # иначе
    print('Нет') # Написать "Нет"
#35 Калькулятор - в задании требовалось создать калькулятор для двух чисел введенных пользователем и математической операции которую тоже вводит пользователь в случае деления на ноль вывести "На ноль делить нельзя"
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
#36 сокрость зум и флеш - в задании нас попросили сравнить скорость этих двух и вывести кто быстрее в случае если скорость одинаковая то требуется вывести сообщение "Не знаю"
n = int(input()) # получаем значение скорости зума
k = int(input()) # получаем значение корости флеша
if n > k: # если скорость флеша больше нежели скорость зума то:
    print('зум быстрее') # написать зум быстрее
elif n < k: # если скорость флеша больше то:
    print('флеш быстрее') # написать флеш быстрее
else: # в другом случае выполнить:
    print('Не знаю') # написать "не знаю"
#37 вид треугольника - в задании требуется определить вид треугольника по введеным трем сторонам и вывести виды в случае соответствия условий
a = int(input()) # получаем первую сторону
b = int(input()) # получаем вторую сторону
c = int(input()) # получаем третью сторону
if (a == b and b != c and a != c) or (a == c and a != b and c != b) or (b == c and b != a and c != a): # если... или ... или... то выполнить:
    print('Равнобедренный') # написать равнобедренный
elif a == b and a == c and c == b: # если ... и ... и ... то выполнить:
    print('Равносторонний') # написать равносторонний
else: # в другом случае выполнить:
    print('Разносторонний') # написать разносторонний
#38 среднее число - в задаче требуется вывести среднее число из трех введеных пользователем
a = int(input()) # получаем первое число
b = int(input()) # получаем второе число
c = int(input()) # получаем третье число
if (a > b and a < c) or (a > c and a < b): # если (a больше b и а меньше с) или (а больше с и а меньше b) то выполнить:
    print(a) # написать а
elif (b > a and b < c) or (b > c and b < a): # если ... или ... то выполнить:
    print(b) # написать b
else: # в другом случае выполнить:
    print(c) # Написать c
#39 В этой программе нам надо узнать среднее число из трех введенных пользователем  
a = int(input("1\n"))
b = int(input("2\n"))
c = int(input("3\n"))
if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
else:
    print(a)
#40 В это программе нам надо узнать количество дней в месяце который ввел пользователь
a = int(input("месяц\n"))
if a == 2:
    print(28)
elif a == 1 or a == 3 or a ==5 or a == 7 or a == 8 or a == 10 or a == 12:
    print(31)
else:
    print(30)
#41 В этом задании нам требуется узнать в какой весовой категории человек
a = int(input("вес\n"))
if a < 60:
    print("Легкий вес")
elif a < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")
#42 здесь нам нужно узнать что будет при смешивании цвета
a = input("цвет 1\n")
b = input("цвет 2\n")
if a == "красный" and b == "синий":
    print("фиолетовый")
elif b== "красный" and a == "синий":
    print("фиолетовый")
elif b == "красный" and a == "желтый":
    print("оранжевый")
elif a == "красный" and b == "желтый":
    print("оранжевый")
elif b == "синий" and a == "желтый":
    print("зеленый")
elif a == "синий" and b == "желтый":
    print("зеленый")
else:
    print("некорректный цвет")

#43 В этом задании нам нужно определить цвет кармана по вводимому номеру или вывести ошибку ввода если число не в диапазоне 0-36
a = int(input("номер кармана\n"))
if a == 0:
    print("зеленый")
elif 1 <= a <= 36:
    if 1 <= a <= 10 or 19 <= a <= 28:
        if a%2 == 0:
            print("черный")
        else:
            print("красный")
    else:
        if a%2 == 1:
            print("черный")
        else:
            print("красный")
else:
    print("ошибка ввода")
    
# Дальше идет контрольная
#1. print()
#2. Верными строками кода являются:
#print('Поэма "Мертвые души" одна из самых интересных')
#print("I'm a math teacher and a programmer!")
#print("3.1415")
#3. Верными строками кода являются:
#print("раз","два","три")
#print('Python','is the best','!!')
#4. Верными строками кода являются:
#print("The World's a little blury", "Or maybe it's my eyes", end='!!!', sep=' :)')
#print("Honey, what's your hurry", end='?')
#print("Told you not to worry", "But maybe that's a lie", sep=')')
#5. Для считывания данных с клавиатуры используется "input()"
#6. "n = int(input())" считывает число в переменную n
#7. Верные утверждения:
#Имя переменной может начинаться с символа подчеркивания(_)
#Имя переменной не может начинаться с цифры
#Имя переменной не может совпадать с ключевым(зарезервированным) словом
#8. Код выведет: 60
#9. Код выведет: 56
#10. Данный код создат прямоугольник из звездочек 17 на 4
for i in range (4):
    print('*'*17)
#11. Данный код выведет квадрат суммы и сумму квадратов двух чисел
a = int(input())
b = int(input())
print("Квадрат суммы",a,"и",b,"равен",(a+b)**2)
print("Сумма квадратов",a,"и",b,"равна",a**2+b**2)
#12. Данный код выведет значение выражения a^b+c^d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a**b)+(c**d))
#13. Данный код выведет число в стиле n+nn+nnn
n = int(input())
if 1<=n<=9:
    print(n,n+1,n+2, sep='')
else:
    print('Число вне диапозона')

#44 в этом задании нам надо считывать длины двух катетов и выводить площадь треугольника
a = int(input())
b = int(input())
print(1/2*a*b)
#45 в программе надо узнать через какое время встретятся старушки имея 2 скорости и расстояние в км 
a  = int(input('v1 '))
b  = int(input('v2 '))
c  = int(input('s '))
v = a+b
v = c/v
print(v)

#46 В задаче требовалось вывести обратное число введенному пользователем, если это число ноль то вывести что числа не существует
a = float(input())
if a>0:
    print(1/a)
else:
    print("Обратного числа не существует")

#47 Нам требовалось найти температуры по градусам цельсия имея температуру в градусах по Фаренгейту
a = int(input())
print((5/9)*(a-32))

#48 Нам требовалось вывести сколько собаке лет по человеческим годам имея готовые формулы
a = int(input())
b = 0
if a > 2:
    b=b+(10.5*2)
    a = a - 2
    b=b + (a*4)
else:
    b = a*10.5
print(b)

#49 Вывести первую точку после запятой
a = float(input())
a = a%1
a = (a*10)//1
print(a)

#50 Нам требуется вывести дробную часть числа
a = float(input())
a = a%1
print(a)

#51 Вывести наибольшее и наименьшее число из пяти введнных пользователем
list1 = list()
min = 999999999
max = 0
for i in range(5):
    a = int(input())
    list1.append(a)
for i in list1:
    if min>i:
        min = i
    if max<i:
        max = i
print('max = ', max)
print('min = ', min)

#52 упорядочивание трехзначных чисел от большего к меньшему
a = int(input())
b = int(input())
c = int(input())
if a > b >c:
    print(a)
    print(b)
    print(c)
elif a > c >b:
    print(a)
    print(c)
    print(b)
elif b>a>c:
    print(b)
    print(a)
    print(c)
elif b>c>a:
    print(b)
    print(c)
    print(a)
elif c>a>b:
    print(c)
    print(a)
    print(b)
elif c>b>a:
    print(c)
    print(b)
    print(a)

#53 интересное число, число является интересным если разость максимальной и минимальной цифры равняется средней по величине цифре
list1=list(input())
list2= list()
for i in list1:
    i = int(i)
    list2.append(i)
if list2[0]-list2[2] == list2[1] or list2[2]-list2[0] == list2[1]:
    print('yes')
else:
    print('no')

#54 требуется чтоб программа считала сумму модулей пяти чисел
a = 0
w = 0
b = list()
while a!=5:
    c = float(input())
    b.append(c)
    a+=1
for i in b:
    if i < 0:
        i = i*(-1)
    w+=i
print(w)

#55
p1 = int(input())
p2 = int(input())
q1= int(input())
q2= int(input())
w = p1-p2
d = q1-q2
if w < 0:
    w = w*-1
if d < 0:
    d = d*-1
print(w+d)

#56
print('"Python is a great language", Said Fred. "I don',"'t ever remeber having this much fun before.",'"', sep="")

#57
a = input()
b = input()
print("Hello",a,b,"! You have just delved into Python")

#58
a = input()
print("Футбольная команда",a,"имеет длину",len(a),"символов")

#59
a = input()
b = input()
c = input()
if len(a)>len(b)>len(c) or len(c)>len(b)>len(a):
    print(a)
    print(c)
elif len(a)>len(c)>len(b) or len(b)>len(c)>len(a):
    print(a)
    print(b)
else:
    print(b)
    print(c)

#60
a = input()
b = input()
c = input()
if len(a)+len(b)==len(c) or len(a)+len(c)==len(b) or len(b)+len(c)==len(a):
    print('yes')
else:
    print('no')

18.
a = input()
if "синий" in a:
    print('ПРЕКРАСНЫЙ ДЕНЬ')
else:
    print('no')

19.
a = input()
if "воскресенье" in a or "суббота" in a:
    print('ЧИЛИМ')
else:
    print('no')

20.
a = input()
if "." in a and "@" in a:
    print('correct')
else:
    print('no')

21.
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
a = (((x1-x2)**2)+((y1-y2)**2))**0.5
print(a)

22.
import math
a = float(input())
print(math.pi*(a**2))
print((math.pi*2)*a)

23.
a = float(input())
b = float(input())
c = 0.5
print('Арифметик ',(a+b)/2)
print('Геометрик ',(a*b)**c)
print('гармоник ', (a*b*2)/(a+b))
print('Квадрат', (((a**2)+(b**2))/2)**c)

24.
import math
x = float(input())
sin1 = math.sin(x)
cos1 = math.cos(x)
tan1 = math.tan(x)**2
print('sin x = ', sin1)
print('cos x = ', cos1)
print('tan^2 x = ', tan1)
r = (x*math.pi)/180
print('r = ',r)

25.
a = float(input())
a = abs(a)
print(a+a)

25(другое решение. В первом перепутал знак со знаком модуля в условии)
a = float(input())
b = 0
if a%1!=0:
    b = a//1
    a = a//1+1
else:
    b = a
print(a+b)

26.
a = float(input())
b = float(input())
c = float(input())
d = ((b**2)-(4*a*c))**0.5
if d > 0:
    x1 = ((b*-1)-d)/(2*a)
    x2 = ((b*-1)+d)/(2*a)
    if x1>x2:
        print(x2,x1)
    else:
        print(x1,x2)
elif d == 0:
    x1 = (b*-1)/(2*a)
    print(x1)
else:
    print('корней нет')

27.
import math
a = float(input())
b = float(input())
s = (a*(b**2)/(4*math.tan(math.pi/a)))
print(s)
