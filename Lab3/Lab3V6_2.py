s = int(input("Введіть число від 0 до 9:"))
if s > 9 or s < 0:
    print("Невірно введене число.")
else:
    for i in range(10):
        if i > s:
            print(i)