"""
Матчасть

Формула точек окружности: (x-xc)^2 + (y-yc)^2 = R^2
(xc, yc) - координаты центра
R - радиус

Формула прямой: (x-xa)^2 + (y-ya)^2 = (x-xb)^2 + (y-yb)^2
(xa, ya) и (xb, yb) - отчки через которые проходит прямая
Частные формулы для прямых, параллельных осям координат: x=xa, y=ya

Алгоритм решения
1) Проверить пересекается ли окружность с прямой проходящей через AB
1.1) В случае пересечения проверить что точка пересечения принадлежит отрезку AB
2) Проверить пересекается ли окружность с прямой проходящей через BC
2.1) В случае пересечения проверить что точка пересечения принадлежит отрезку BC
3) Проверить пересекается ли окружность с прямой проходящей через CD
3.1) В случае пересечения проверить что точка пересечения принадлежит отрезку CD
4) Проверить пересекается ли окружность с прямой проходящей через DA
4.1) В случае пересечения проверить что точка пересечения принадлежит отрезку DA

Решение:
Прямая, проходящая через AB: x=1
Отрезок AB: (-1 <= y <= 1)
Прямая, проходящая через BC: y=-1
Отрезок BC: (-1 <= x <= 1)
Прямая, проходящая через CD: x=-1
Отрезок CD: (-1 <= y <= 1)
Прямая, проходящая через DA: y=1
Отрезок DA: (-1 <= x <= 1)

Итого результирующие уравнения:
Для AB:
(1-xc)^2 + (y-yc)^2 = R^2
1 - 2*xc + xc^2 + y^2 - 2*y*yc + yc^2 = R^2
y^2 - 2*yc*y + 1 - 2*xc + xc^2 + yc^2 - R^2 = 0

Для BC:
(x-xc)^2 + (-1-yc)^2 = R^2
x^2 - 2*xc*x + xc^2 + 1 + 2*yc + yc^2 - R^2 = 0

Для CD:
(-1-xc)^2 + (y-yc)^2 = R^2
1 + 2*xc + xc^2 + y^2 - 2*yc*y + yc^2 = R^2
y^2 - 2*yc*y + 1 + 2*xc + xc^2 + yc^2 - R^2 = 0

Для DA:
(x-xc)^2 + (1-yc)^2 = R^2
x^2 - 2*xc*x + xc^2 + 1 - 2*yc + yc^2 - R^2 = 0


"""

import math

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

if __name__ == '__main__':
    xc = float(input('Введите x центра окружности '))
    yc = float(input('Введите y центра окружности '))
    R = float(input('Введите радиус окружности '))

    # Список коэффициентов
    segments = (
        (1, -2*yc, 1-2*xc+xc*xc+yc*yc-R*R, "AB", "y"),  # Для отрезка AB
        (1, -2*xc, xc*xc+1+2*yc+yc*yc-R*R, "BC", "x"),  # Для отрезка BC
        (1, -2*yc, 1+2*xc+xc*xc+yc*yc-R*R, "CD", "y"),  # Для отрезка CD
        (1, -2*xc, xc*xc+1-2*yc+yc*yc-R*R, "DA", "x"),  # Для отрезка DA
    )

    interception = False

    for segment in segments:
        current_interception = False

        result =  equationroots(
                        segment[0],
                        segment[1],
                        segment[2]
                    )

        print("{axis}-координаты пересечений прямой {seg}: {res}".format(
                                        axis=segment[4],
                                        seg=segment[3],
                                        res=result
                                    ), end=',')

        if result is not None:
            # Если пересеклись с прямой проверяем принадлежность отрезку точек пересечения
            if (result[0] > -1 and result[0] < 1) or (result[1] > -1 and result[1] < 1):
                interception = True
                current_interception = True

        if current_interception:
            print(' отрезок {seg} - пересекается'.format(seg=segment[3]))
        else:
            print(' отрезок {seg} - не пересекается'.format(seg=segment[3]))

    if interception:
        print("Окружность и квадрат - пересекаются")
    else:
        print("Окружность и квадрат - не пересекаются")