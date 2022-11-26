#code for the calculator's GUI
from tkinter import * #import tkinter
root = Tk()
root.geometry("940x587")
bg = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Calculator.png")
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