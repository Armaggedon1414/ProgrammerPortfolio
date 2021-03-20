# Jadiah Jensen, Caleb Keller
# 1/20/21
# Class GUI
from tkinter import *

class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.numb = 9
        self.config(bg="Black")
        self.grid()
        self.bttnList = []
        self.createWidgets()
        self.equation = ""

    def createWidgets(self):
        self.entryTxt = ""
        self.entry1 = Entry(self, text=self.entryTxt, bg="black", fg="red")
        self.entry1.grid(row=0, column=0, columnspan=4)

        for r1 in range(3):
            for c1 in range(3):
                nmbr = ("     " + str(self.numb) + "     ")
                self.button = Button(self, text=nmbr, bg="Black", fg="Red")
                self.button.grid(row=(r1+1), column=(2-c1))
                self.bttnList.append(self.button)
                self.numb -= 1

        for c2 in range(3):
            txt = ""
            if c2 == 0:
                txt = "     0     "
            elif c2 == 1:
                txt = "      .      "
            elif c2 == 2:
                txt = "ENTER"
            self.button1 = Button(self, text=txt, bg="Black", fg="Red")
            self.button1.grid(row=4, column=c2)
            self.bttnList.append(self.button1)

        for r2 in range(5):
            sign = ""
            if r2 == 0:
                sign = " + "
            elif r2 == 1:
                sign = " - "
            elif r2 == 2:
                sign = " x "
            elif r2 == 3:
                sign = " / "
            elif r2 == 4:
                sign = "<x"
            self.button2 = Button(self, text=sign, bg="Black", fg="Red")
            self.button2.grid(row=r2, column=4)
            self.bttnList.append(self.button2)


        self.bttnList[0].config(command=self.num9)
        self.bttnList[1].config(command=self.num8)
        self.bttnList[2].config(command=self.num7)
        self.bttnList[3].config(command=self.num6)
        self.bttnList[4].config(command=self.num5)
        self.bttnList[5].config(command=self.num4)
        self.bttnList[6].config(command=self.num3)
        self.bttnList[7].config(command=self.num2)
        self.bttnList[8].config(command=self.num1)
        self.bttnList[9].config(command=self.num0)
        self.bttnList[10].config(command=self.deciPoint)
        self.bttnList[11].config(command=self.enter)
        self.bttnList[12].config(command=self.add)
        self.bttnList[13].config(command=self.sbtrct)
        self.bttnList[14].config(command=self.mult)
        self.bttnList[15].config(command=self.divide)
        self.bttnList[16].config(command=self.clear)

    def createButtons(self, c, r, num):
        Button(self, text=num, bg="Black", fg="Red").grid(column=c, row=r)

    def createEntry(self, txt, r, c, bg="black", fg="red", cs=3):
        entry = Entry(self,
                      text=txt,
                      bg=bg,
                      fg=fg
                      ).grid(row=r,
                             column=c,
                             columnspan=cs)
        return entry

    def num9(self):
        self.entryTxt = "9"
        self.equation += "9"
        self.entry1.insert(END, self.entryTxt)

    def num8(self):
        self.entryTxt = "8"
        self.equation += "8"
        self.entry1.insert(END, self.entryTxt)

    def num7(self):
        self.entryTxt = "7"
        self.equation += "7"
        self.entry1.insert(END, self.entryTxt)

    def num6(self):
        self.entryTxt = "6"
        self.equation += "6"
        self.entry1.insert(END, self.entryTxt)

    def num5(self):
        self.entryTxt = "5"
        self.equation += "5"
        self.entry1.insert(END, self.entryTxt)

    def num4(self):
        self.entryTxt = "4"
        self.equation += "4"
        self.entry1.insert(END, self.entryTxt)

    def num3(self):
        self.entryTxt = "3"
        self.equation += "3"
        self.entry1.insert(END, self.entryTxt)

    def num2(self):
        self.entryTxt = "2"
        self.equation += "2"
        self.entry1.insert(END, self.entryTxt)

    def num1(self):
        self.entryTxt = "1"
        self.equation += "1"
        self.entry1.insert(END, self.entryTxt)

    def num0(self):
        self.entryTxt = "0"
        self.equation += "0"
        self.entry1.insert(END, self.entryTxt)

    def deciPoint(self):
        self.entryTxt = "."
        self.equation += "."
        self.entry1.insert(END, self.entryTxt)

    def enter(self):
        try:
            Equals = eval(self.equation)
            self.entry1.delete(0, END)
            self.entry1.insert(0, str(Equals))
        except:
            self.entry1.delete(0, END)
            self.entry1.insert(0, "Cannot Compute")

    def add(self):
        self.entryTxt = "+"
        self.equation += "+"
        self.entry1.insert(END, self.entryTxt)

    def sbtrct(self):
        self.entryTxt = "-"
        self.equation += "-"
        self.entry1.insert(END, self.entryTxt)

    def mult(self):
        self.entryTxt = "*"
        self.equation += "*"
        self.entry1.insert(END, self.entryTxt)

    def divide(self):
        self.entryTxt = "/"
        self.equation += "/"
        self.entry1.insert(END, self.entryTxt)

    def clear(self):
        self.equation = ""
        self.entry1.delete(0, END)

def main():
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)
    root.config(bg="Black")
    root = App(root)
    root.mainloop()

main()
