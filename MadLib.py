# Mad Libs
# 2/17/2021
# Jadiah Jensen, Caleb Keller

from tkinter import *

HEIGHT = 400
WIDTH = 700
TITLE = "Mad Lib"
BACKGROUND = "Black"

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.config(bg="Black")
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        self.partsList = []

        lbln1 = Label(self, text="Noun(Place)", bg="Black", fg="Red")
        lbln1.grid(row=0, column=0)
        self.noun1 = Entry(self, bg="Black", fg="Red")
        self.noun1.grid(row=0, column=1, columnspan=2)

        lbln2 = Label(self, text="Noun(Animal)", bg="Black", fg="Red")
        lbln2.grid(row=1, column=0)
        self.noun2 = Entry(self, bg="Black", fg="Red")
        self.noun2.grid(row=1, column=1, columnspan=2)

        lbla1 = Label(self, text="Adjective", bg="Black", fg="Red")
        lbla1.grid(row=2, column=0)
        self.adj1 = Entry(self, bg="Black", fg="Red")
        self.adj1.grid(row=2, column=1, columnspan=2)

        lblbP = Label(self, text="Noun(Body Part)", bg="Black", fg="Red")
        lblbP.grid(row=3, column=0)
        self.bodyPart = Entry(self, bg="Black", fg="Red")
        self.bodyPart.grid(row=3, column=1, columnspan=2)

        lblname = Label(self, text="Name", bg="Black", fg="Red")
        lblname.grid(row=4, column=0)
        self.name = Entry(self, bg="Black", fg="Red")
        self.name.grid(row=4, column=1, columnspan=2)

        lbln3 = Label(self, text="Noun(plural)", bg="Black", fg="Red")
        lbln3.grid(row=5, column=0)
        self.noun3 = Entry(self, bg="Black", fg="Red")
        self.noun3.grid(row=5, column=1, columnspan=2)

        lblplace = Label(self, text="Noun(Place)", bg="Black", fg="Red")
        lblplace.grid(row=6, column=0)
        self.place = Entry(self, bg="Black", fg="Red")
        self.place.grid(row=6, column=1, columnspan=2)

        lblv1 = Label(self, text="Verb", bg="Black", fg="Red")
        lblv1.grid(row=7, column=0)
        self.verb1 = Entry(self, bg="Black", fg="Red")
        self.verb1.grid(row=7, column=1, columnspan=2)

        lbln3 = Label(self, text="Noun(plural)", bg="Black", fg="Red")
        lbln3.grid(row=8, column=0)
        self.noun4 = Entry(self, bg="Black", fg="Red")
        self.noun4.grid(row=8, column=1, columnspan=2)

        lblv2 = Label(self, text="Verb(Past Tense)", bg="Black", fg="Red")
        lblv2.grid(row=9, column=0)
        self.verb2 = Entry(self, bg="Black", fg="Red")
        self.verb2.grid(row=9, column=1, columnspan=2)

        lblv3 = Label(self, text="Verb", bg="Black", fg="Red")
        lblv3.grid(row=10, column=0)
        self.verb3 = Entry(self, bg="Black", fg="Red")
        self.verb3.grid(row=10, column=1, columnspan=2)

        start = Button(self, text="See Story", command = self.getStory, bg="Black", fg="Red")
        start.grid(row=11, column=1)

        self.showStory = Text(self, bg="Black", fg="White")
        self.showStory.grid(row=12, column=0, rowspan=2, columnspan=4)

    def getStory(self):
        noun1 = self.noun1.get()
        noun2 = self.noun2.get()
        adj1 = self.adj1.get()
        bodyPart = self.bodyPart.get()
        name = self.name.get()
        noun3 = self.noun3.get()
        place = self.place.get()
        verb1 = self.verb1.get()
        noun4 = self.noun4.get()
        verb2 = self.verb2.get()
        verb3 = self.verb3.get()
        story = str.format("""In the {0}, there was a {1} with a {2} {3}. 
        The {1} gazed deeply into {4}'s eyes filling him with fear. 
        {4} knew it was the end for him. As {5} fell upon the surface 
        of the {6}, {4} began {7} quickly away from the {1}, hoping 
        to escape his {8}. {4} {9}, falling onto the floor and then
        {10}ed""", noun1, noun2, adj1, bodyPart, name, noun3, place, verb1, noun4, verb2, verb3)
        self.showStory.insert(END, story)
        print(story)


def main():
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.config(bg=BACKGROUND)
    root = App(root)
    root.mainloop()


main()
