from tkinter import *

window = Tk()
window.title("New")
window.minsize(width=1000, height=300)

#Label
lbl = Label(text="I'm a label working as it should", font=("Arial", 24, "bold"))
lbl.grid(row=0, column=0)


def button_clicked():
    lbl.config(text=f"{input.get()}")

new_button = Button(text="Click me", command=button_clicked)
new_button.grid(row=0, column=1)

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

input = Entry(width=20)
input.grid(row=2, column=2)

window.mainloop()
