import AreaTriangle as at

side = int(input("Введіть сторону трикутника:"))
if side <= 0:
    print("Сторона трикутника не може бути менша або дорівнювати 0!")
else:
    f_angle = int(input("Введіть перший кут:"))
    s_angle = int(input("Введіть другий кут:"))
    if f_angle or s_angle < 0:
        print("Кути трикутника не можуть бути від'ємними!")
    else:
        a = at.area(side, f_angle, s_angle)
        print("Ви ввели сторону a: {}, кут A: {}, кут B: {}".format(side, f_angle, s_angle))
        print("Площа трикутника: {}".format(round(a, 2)))
