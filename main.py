#1 Задание
s = 0
k = 15
d = k-10
def ff():
    k = 4*d
    s = k-50
    print(s)
ff()

#2 Задание

x = 3
y = 4
z = x+y
def cc():
    b = z+1
    x = 4
    y = 5
    x = b+y+7
    print(x)
cc()

#3 Задание

n = int(input())
for k in range(n, n + 3):
    print(k)

#4 Задание

p = int(input())
o = int(input())
i = int(input())
m = p+o+i
print(m)

#5 Задание

l = int(input())
def ss():
    V = l**3
    s = 6*l**2
    print(V)
    print(s)
ss()

#6 Задание

g = int(input())
h = int(input())
def zf():
    q = 3*(g+h)**3+275*h**2-127*g-41
    print(q)
zf()

#7 Задание
t = int(input())
def ps():
    global t
    y = t + 1
    print("Следующее за числом ", t, "число ", y)
ps()
def pp():
    global t
    py = t - 1
    print("Предыдущее за числом ", t, "число ", py)
pp()

8 Задание
pc = int(input())
mnt = int(input())
klv = int(input())
msh = int(input())
def stoim():
    stoma = (pc+mnt+klv+msh)*3
    print(stoma)
stoim()
#9 zadanie
a = int(input())
b = int(input())
def i ():
    z = a+b
    x = a-b
    c = a*b
    print(a, "+", b, "=", z)
    print(a, "-", b, "=", x)
    print(a, "*", b, "=", c)
i()
# 10
c = int(input())
b = int(input())
a = int(input())
def i():
    ar = (2 * a + (b - 1) * c) * b / 2
    print(int(ar))
i()
11
x = int(input())
def i():
    xx = 2*x
    xxx = 3*x
    xxxx = 4*x
    xxxxx = 5*x
    print(x,"---", xx,"---", xxx,"---", xxxx,"---", xxxxx)
i()

#12
a = int(input())
b = int(input())
c = int(input())
def i():
    sum = a*b**(c-1)
    print(sum)
i()

#13
a = int(input())
def i ():
    z = a/100
    print(int(z))
i()

#14
n = int(input())
k = int(input())
def i ():
    z=k%n
    print(z)
i()
