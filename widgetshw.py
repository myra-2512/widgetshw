from tkinter import *

window = Tk()
window.title("Product Calculator")
window.geometry("400x400")

lbl1=Label(text="Enter First Number:",bg="lavender",fg="black")
entry1=Entry()
lbl2=Label(text="Enter Second Number:",bg="lavender",fg="black")

entry2=Entry()


btn=Button(text="Calculate Product",bg="lightgreen",fg="black")

result_box=Text(height=3)

def calculate_product():
    num1=entry1.get()
    num2=entry2.get()

    product = float(num1) * float(num2)
    result_box.insert(END, "The product is: " + str(product) + "\n")
    
    
btn.config(command=calculate_product)

lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
btn.pack()
result_box.pack()

window.mainloop()