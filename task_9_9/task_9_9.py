#coding: utf-8

"""
Решаем уравнение
x^4 + ax^3 + bx^2 + cx + d = 0

1) Вводим p,q,r

Кубическая резольвента
2s^3 - ps^2 - 2rs + rp -q^2/4 = 0
s^3 - (p/2)*s^2 - rs + rp/2 - q^2/8 = 0

"""
import math

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
d = float(input('Введите d: '))

#a,b,c,d = (4,-4,-20,-5)

p = b - a*a*3/8
q = a*a*a/8 - a*b/2 + c
r = -a*a*a*a*3/256 + a*a*b/16 - a*c/4 + d


# x^3 + ax^2 + bx + c = 0
def solve_equation(a,b,c,x):
    return x**3 + a*x**2 + b*x + c

# Проверяем какой из делителей свободного члена уравнения является целым корнем уравнения
def solve_cube(a, b, c):
    for i in range(2, int(abs(c))):
         if solve_equation(a,b,c,i) == 0:
             return i
         if solve_equation(a,b,c,-i) == 0:
             return -i

    return None

def solve_something(p,q,r):
    a1 = -p/2
    b1 = -r
    c1 = r*p/2 - q*q/8
    # print(p, q, r)
    # print(a1, b1, c1)
    return solve_cube(a1, b1, c1)

# function for finding roots
def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c

    if dis < 0:
        return None

    sqrt_val = math.sqrt(abs(dis))
    root1 = 0
    root2 = 0

    # checking condition for discriminant
    if dis > 0:
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)

    elif dis == 0:
        root1 = root2 = -b / (2 * a)

    return (root1, root2)

s = solve_something(p,q,r)

y1, y2 = equationroots(
    1,
    - math.sqrt(2*s - p),
    q/(2*math.sqrt(2*s-p)) + s
)

y3, y4 = equationroots(
    1,
    math.sqrt(2*s - p),
    -q/(2*math.sqrt(2*s-p)) + s
)

def get_x(y,a):
    return y-a/4

print(get_x(y1,a), get_x(y2,a), get_x(y3,a), get_x(y4,a))


