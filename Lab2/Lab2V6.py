def avg(first, second, third):
    s = (first + second + third) / 3
    return s


a = int(input("Введіть перше ціле число:"))
b = int(input("Введіть друге ціле число:"))
c = int(input("Введіть третє ціле число:"))

avg = round(avg(a, b, c), 2)

print("({}+{}+{})/3 = {} - середнє арифметичне".format(a, b, c, avg))