#code for the calculator's GUI
from tkinter import *
root = Tk()
root.geometry("1200x750")

#calculator as bg image 
bg = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Calculator.png")
label = Label(root, image = bg)
label.place(x = 0, y = 0)

image1x1 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x1 n (12x).png")

#buttons for the calculator
frame = Frame(root)
frame.pack

Button(frame, image = image1x1).pack(side = LEFT)
root.mainloop()

#26/11/22: attempt to program RPN for calculator
#def RPN():
#    stm = True
#    while stm:
#        list = []
#        try:
#            x = int(input())
#            list.append(x)
#        except:
#            stm = False
#        return list
#print(RPN())