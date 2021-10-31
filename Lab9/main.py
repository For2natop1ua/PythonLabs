from tkinter import *


def display_avg():
    result_entry.delete(0, END)
    result_entry.insert(0, round(((first.get() + second.get() + third.get()) / 3), 2))


root = Tk()
root.title("Лабораторна робота №9")

first = IntVar()
second = IntVar()
third = IntVar()
result = IntVar()

first_label = Label(text="a:")
second_label = Label(text="b:")
third_label = Label(text="c:")
result_label = Label(text="Результат:")

first_label.grid(row=0, column=0, sticky="w")
second_label.grid(row=1, column=0, sticky="w")
third_label.grid(row=2, column=0, sticky="w")
result_label.grid(row=3, column=0, sticky="w")

first_entry = Entry(textvariable=first)
second_entry = Entry(textvariable=second)
third_entry = Entry(textvariable=third)
result_entry = Entry(textvariable=result)

first_entry.grid(row=0, column=1, padx=5, pady=5)
second_entry.grid(row=1, column=1, padx=5, pady=5)
third_entry.grid(row=2, column=1, padx=5, pady=5)
result_entry.grid(row=3, column=1, padx=5, pady=5)

message_button = Button(text="Порахувати", command=display_avg)
message_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

first_entry.delete(0, END)
second_entry.delete(0, END)
third_entry.delete(0, END)
result_entry.delete(0, END)

root.mainloop()
