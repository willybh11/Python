
from Tkinter import *

def getList():

    with open("phones.txt") as f:
        out = []
        for n in f.readlines():
            out.append(n.strip("\n").split("|"))
    return out


class PhoneBook(Frame):

    def whichSelected(self):
        return int(self.select.curselection()[0])

    def addEntry(self):
        if len(self.nameVar.get()) == 0:
            print "You still have to enter a name!"
            return
        if len(self.phoneVar.get()) == 0:
            print "You still have to enter a number!"
            return
        phonelist.append([self.nameVar.get(), self.phoneVar.get()])
        self.setSelect()

    def deleteEntry(self):
        try:
            del phonelist[self.whichSelected()]
            self.setSelect()
        except IndexError:
            print "You still have to select something!"

    def updateEntry(self):
        try:
            phonelist[self.whichSelected()] = [self.nameVar.get(), self.phoneVar.get()]
            self.setSelect()
        except IndexError:
            print "You still have to select something!"

    def loadEntry(self):
        try:
            name, phone = phonelist[self.whichSelected()]
            self.nameVar.set(name)
            self.phoneVar.set(phone)
        except IndexError:
            print "You still have to select something!"

    def setSelect(self):
        phonelist.sort()
        self.select.delete(0,END)
        for name,phone in phonelist:
            self.select.insert(END,name)


    def makeLabels(self):

        self.NAME = Label(self)
        self.NAME["text"] = "Name"
        self.NAME.grid(row=0,column=0,sticky=W)

        self.nameVar = StringVar()
        self.name = Entry(self)
        self.name["textvariable"] = self.nameVar
        self.name.grid(row=0,column=1,columnspan=2,sticky=W)

        self.PHONE = Label(self)
        self.PHONE["text"] = "Phone"
        self.PHONE.grid(row=1,column=0,sticky=W)

        self.phoneVar = StringVar()
        self.phone = Entry(self)
        self.phone["textvariable"] = self.phoneVar
        self.phone.grid(row=1,column=1,columnspan=2,sticky=W)

    def makeButtons(self):

        self.A_Button = Button(self)
        self.A_Button["text"] = " Add  "
        self.A_Button["command"] = self.addEntry
        self.A_Button.grid(row=2,column=0,sticky=W+E)

        self.D_Button = Button(self)
        self.D_Button["text"] = "Delete"
        self.D_Button["command"] = self.deleteEntry
        self.D_Button.grid(row=2,column=1,sticky=W+E)

        self.U_Button = Button(self)
        self.U_Button["text"] = "Update"
        self.U_Button["command"] = self.updateEntry
        self.U_Button.grid(row=2,column=2,sticky=W+E)

        self.L_Button = Button(self)
        self.L_Button["text"] = " Load "
        self.L_Button["command"] = self.loadEntry
        self.L_Button.grid(row=2,column=3,sticky=W+E)

        self.Q_Button = Button(self)
        self.Q_Button["text"] = " QUIT "
        self.Q_Button["fg"] = "red"
        self.Q_Button["command"] = self.quit
        self.Q_Button.grid(row=0,column=3,rowspan=2,sticky=S+N)


    def makeSidebar(self):

        self.scroll = Scrollbar(self)
        self.select = Listbox(self)
        self.select["yscrollcommand"] = self.scroll.set
        self.select["height"] = 6
        self.scroll["command"] = self.select.yview

        self.scroll.grid(row=3,column=3,sticky=N+S+W+E)
        self.select.grid(row=3,column=0,columnspan=3,sticky=W+E+S+N)


    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.grid()
        self.master.title("Phonebook")
        self.makeLabels()
        self.makeButtons()
        self.makeSidebar()
        self.setSelect()

phonelist = getList()
root = Tk()
app = PhoneBook(master=root)
app.mainloop()
root.destroy()
