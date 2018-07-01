from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_val.get())
    miles = float(e1_val.get()) * 1.6
    t1.insert(END, miles)


b1 = Button(window,text="Convert to miles", command=km_to_miles)
b1.grid(row=0, column=2)

l5 = Label(window, text="Km->")
l5.grid(row=0, column=0)
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

l6 = Label(window, text="miles")
l6.grid(row=0, column=3)
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=4)


def kg_conversion():
    grams = float(e2_val.get()) * 1000
    pounds = float(e2_val.get()) * 2.20462
    ounces = float(e2_val.get()) * 35.274

    t2.insert(END,grams)
    t3.insert(END,pounds)
    t4.insert(END,ounces)

l1 = Label(window, text="Kilogram ->")
l1.grid(row=1, column=0)

e2_val = StringVar()
e2 = Entry(window, textvariable=e2_val)
e2.grid(row=1, column=1)

b2 = Button(window,text="Covert", command=kg_conversion)
b2.grid(row=1, column=2)

l2 = Label(window, text="grams")
l2.grid(row=2, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=3, column=0)

l3 = Label(window, text="pounds")
l3.grid(row=2, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=3, column=1)

l4 = Label(window, text="ounces")
l4.grid(row=2, column=2)
t4 = Text(window, height=1, width=20)
t4.grid(row=3, column=2)

window.mainloop()