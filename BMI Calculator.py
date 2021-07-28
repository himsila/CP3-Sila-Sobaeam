from tkinter import*
import math

#Def function
def BMICal(event):
    BMI = float(textboxWeight.get())/math.pow(float(textboxHeight.get())*(math.pow(10,-2)),2)
    if BMI >= 30 :
        Result = "อ้วนมาก"
    elif BMI >= 25 :
        Result = "อ้วน"
    elif BMI >= 23 :
        Result = "น้ำหนักเกิน"
    elif BMI >= 18.6 :
        Result = "น้ำหนักปกติ"
    else :
        Result = "ผอมเกินไป"
    labelResult.configure(text= f"{BMI:.2f}, คุณอยู่ในสภาวะ {Result}")

#Create Userform
parent = Tk()

#Create Widget
labelHeight = Label(parent,
                    text = "ส่วนสูง (cm.)")
labelHeight.grid(row = 0, column = 0)
labelWeight = Label(parent,
                    text = "น้ำหนัก (kg.)")
labelWeight.grid(row = 1, column = 0)
labelResult = Label(parent,
                    text = "ผลลัพธ์")
labelResult.grid(row = 2, column = 1)

textboxHeight = Entry(parent)
textboxHeight.grid(row = 0, column = 1)
textboxWeight = Entry(parent)
textboxWeight.grid(row = 1, column = 1)

buttonCal = Button(parent,
                   text = "คำนวณ")
buttonCal.grid(row = 2 , column = 0)

#Bind Function
buttonCal.bind('<Button-1>', BMICal)

#Launch Userform
parent.mainloop()