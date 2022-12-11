#code for the calculator's GUI
from tkinter import *
import math

root = Tk()
root.geometry("1200x750")
root.title("Financial calculator")
root.resizable(width=False, height=False)

font1 = "Arial 50"
font2 = "Arial 30"

opt = StringVar()
opt.set("")
spt = StringVar()
spt.set("[ ]")
sqc = ''
stacklbl = Label(root, text = "Stack: ", font = font2, width = 6, anchor = W)
stacklbl.place(x = 71, y = 143)
display = Label(root, textvariable = opt, font = font1, borderwidth = 5, relief = "groove", width = 27, anchor = E)
display.place(x = 77, y = 43)
stackdisplay = Label(root, textvariable = spt, font = font2, borderwidth = 5, relief = "groove", width = 41, anchor = W)
stackdisplay.place(x = 187, y = 140)

#Functions of the Calculaor
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
operators = ["+", "-", "*", "/", "1/x", "+/-", "y^x", "%", "e^x"]
others = ["C", "ENTER", "REG", "SWAP"]
stack = [] 
operationPressed = False
isAnErrorHappened = False
f_function = False
g_function = False
errorMessages = {"stackError": "Error: not enough args in stack",
                     "divisionByZero": "Error: division by zero ",
                     "domainError": "Error: cannot complete calculation",
                     "overflow": "Error: oveflow"}

#main function hub
def function(x):
    global isAnErrorHappened
    global operationPressed
    global errorMessages
    global opt
    global stack
    if x in digits:
        if isAnErrorHappened:
            press_C()
        if operationPressed:
            press_ENTER()
            press_C()
        if isinstance(x, Event): # Input via keyboard rather than clicking on app
            x = chr(x)
        if not(x == "." and x in opt.get()): 
            press_num(x)
    if x in operators:
        if opt.get() in errorMessages.values():
            return
        try:
            if isinstance(x, Event): # Input via keyboard rather than clicking on app
                x = chr(x)
            if x in ["+", "-", "*", "/", "y^x", "%"]:
                if opt.get():
                    x = float(opt.get())
                    y = float(stack.pop())
                else:
                    x = float(stack.pop())
                    y = float(stack.pop())
                if x == "+":
                    opt.set((round(y + x, 10)))                       
            
        except IndexError:  # There isn't enough args in the stack to do the operation
            press_ENTER()
            opt.set(errorMessages["stackError"])
            isAnErrorHappened = True
            
        except ZeroDivisionError:  # Division by zero
            opt.set(errorMessages["divisionByZero"])
            isAnErrorHappened = True
            
        except ValueError:
            opt.set(errorMessages["domainError"])
            isAnErrorHappened = True
            
        except OverflowError:
            opt.set(errorMessages["overflow"])
            isAnErrorHappened = True
            

#individual buttons / commands
def press_f():
    global button3x5
    global f_function
    f_function = True
    if f_function:
        button3x5 = Button(root, image = image3x5, command = lambda: press_REG())

        
def press_C():
    global sqc
    opt.set("")
    sqc = ''

def press_ENTER():
    if opt.get() and opt.get() not in errorMessages.values():
        refresh_stack_display() 



#outside commands
def press_num(num):
    global sqc
    sqc = sqc + str(num)
    opt.set(sqc)

def press_REG():
    global stack
    global sqc
    opt.set("")
    spt.set("[ ]")
    sqc = ''
    stack = []

def refresh_stack_display():
    global sqc
    global stack
    if stack == []:
        stack = [opt.get()]
        spt.set(stack)
        press_C()
    else:
        stack.append(opt.get())
        spt.set(stack)
        press_C()



#calculator as bg image 
bg = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Calculator.png")
label = Label(root, image = bg)
label.place(x=1, y=215)

#images for the buttons
image1x1 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x1 n (12x).png")
image1x2 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x2 i (12dif).png")
image1x3 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x3 PV (CFo).png")
image1x4 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x4 PMT (CFj).png")
image1x5 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x5 FV (Nj).png")
image1x6 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x6 CHS (DATE).png")
image1x7 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x7 7 (BEG).png")
image1x8 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x8 8 (END).png")
image1x9 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x9 9 (MEM).png")
image1x10 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\1x10 sym divide.png")
image2x1 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x1 Y^x (sqrt(X)).png")
image2x2 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x2 Recip(x) (e^x).png")
image2x3 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x3 Total% (LN).png")
image2x4 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x4 Delta% (FRAC).png")
image2x5 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x5 % (INTG).png")
image2x6 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x6 EEX (DeltaDays).png")
image2x7 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x7 4 (D.MY).png")
image2x8 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x8 5 (M.DY).png")
image2x9 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x9 6 (Xbar W).png")
image2x10 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\2x10 sym mul.png")
image3x1 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x1 Run-Stop (PSE).png")
image3x2 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x2 Single Step (BST).png")
image3x3 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x3 R Down (Go-to).png")
image3x4 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x4 X switch Y (X less_ Y).png")
image3x5 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x5 Clear (X=0).png")
image3x6 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x6 ENTER (LSTx).png")
image3x7 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x7 1 (Xconst r).png")
image3x8 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x8 2 (Yconst r).png")
image3x9 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x9 3 (n!).png")
image3x10 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\3x10 sym minus (del).png")
image4x1 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x1 ON.png")
image4x2 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x2 shift F.png")
image4x3 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x3 Shift G.png")
image4x4 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x4 Store.png")
image4x5 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x5 Recall.png")
image4x7 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x7 0 (Xbar).png")
image4x8 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x8 Decimal (S).png")
image4x9 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x9 Sum+ (Sum-).png")
image4x10 = PhotoImage(file = "C:\\Users\\Key\\Desktop\\PyProFE\\PyProjectFE\\Buttons\\4x10 sym plus.png")

#buttons for the calculator
button1x1 = Button(root, image = image1x1)
button1x1.place(x=73, y=257)
button1x2 = Button(root, image = image1x2)
button1x2.place(x=183, y=257)
button1x3 = Button(root, image = image1x3)
button1x3.place(x=290, y=257)
button1x4 = Button(root, image = image1x4)
button1x4.place(x=399, y=257)
button1x5 = Button(root, image = image1x5)
button1x5.place(x=505, y=257)
button1x6 = Button(root, image = image1x6)
button1x6.place(x=614, y=257)
button1x7 = Button(root, image = image1x7, command = lambda: function('7'))
button1x7.place(x=721, y=257)
button1x8 = Button(root, image = image1x8, command = lambda: function('8'))
button1x8.place(x=828, y=257)
button1x9 = Button(root, image = image1x9, command = lambda: function('9'))
button1x9.place(x=936, y=257)
button1x10 = Button(root, image = image1x10)
button1x10.place(x=1044, y=257)
button2x1 = Button(root, image = image2x1)
button2x1.place(x=73, y=377)
button2x2 = Button(root, image = image2x2)
button2x2.place(x=183, y=377)
button2x3 = Button(root, image = image2x3)
button2x3.place(x=290, y=377)
button2x4 = Button(root, image = image2x4)
button2x4.place(x=399, y=377)
button2x5 = Button(root, image = image2x5)
button2x5.place(x=505, y=377)
button2x6 = Button(root, image = image2x6)
button2x6.place(x=614, y=377)
button2x7 = Button(root, image = image2x7, command = lambda: function('4'))
button2x7.place(x=721, y=377)
button2x8 = Button(root, image = image2x8, command = lambda: function('5'))
button2x8.place(x=828, y=377)
button2x9 = Button(root, image = image2x9, command = lambda: function('6'))
button2x9.place(x=936, y=377)
button2x10 = Button(root, image = image2x10)
button2x10.place(x=1044, y=377)
button3x1 = Button(root, image = image3x1)
button3x1.place(x=73, y=497)
button3x2 = Button(root, image = image3x2)
button3x2.place(x=183, y=497)
button3x3 = Button(root, image = image3x3)
button3x3.place(x=290, y=497)
button3x4 = Button(root, image = image3x4)
button3x4.place(x=399, y=497)
button3x5 = Button(root, image = image3x5, command = lambda: press_C())
button3x5.place(x=505, y=497)
button3x6 = Button(root, image = image3x6, command = lambda: press_ENTER())
button3x6.place(x=614, y=497)
button3x7 = Button(root, image = image3x7, command = lambda: function('1'))
button3x7.place(x=721, y=497)
button3x8 = Button(root, image = image3x8, command = lambda: function('2'))
button3x8.place(x=828, y=497)
button3x9 = Button(root, image = image3x9, command = lambda: function('3'))
button3x9.place(x=936, y=497)
button3x10 = Button(root, image = image3x10)
button3x10.place(x=1044, y=497)
button4x1 = Button(root, image = image4x1)
button4x1.place(x=73, y=615)
button4x2 = Button(root, image = image4x2, command = lambda: press_f())
button4x2.place(x=183, y=615)
button4x3 = Button(root, image = image4x3)
button4x3.place(x=290, y=615)
button4x4 = Button(root, image = image4x4)
button4x4.place(x=399, y=615)
button4x5 = Button(root, image = image4x5)
button4x5.place(x=505, y=615)
button4x7 = Button(root, image = image4x7, command = lambda: function('0'))
button4x7.place(x=721, y=615)
button4x8 = Button(root, image = image4x8, command = lambda: function('.'))
button4x8.place(x=828, y=615)
button4x9 = Button(root, image = image4x9)
button4x9.place(x=936, y=615)
button4x10 = Button(root, image = image4x10, command = lambda: function("+"))
button4x10.place(x=1044, y=615)

root.mainloop()