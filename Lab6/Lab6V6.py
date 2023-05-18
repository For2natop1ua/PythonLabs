import random


def createFile(myFile, q):
    with open(myFile, "w") as outFile:
        outFile.writelines(["{}\n".format(x) for x in random.sample(range(0, 101, 2), q)])


n = int(input("Введіть скільки випадкових цілих парних чисел треба записати у файл\n"))
createFile("foo.txt", n)
