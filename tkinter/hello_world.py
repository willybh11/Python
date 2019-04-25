from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})

    def createEntrythingy(self):
        self.entrythingy = Entry()
        self.entrythingy.pack({"side":"top"})

        self.contents = StringVar()
        self.contents.set("type in 'options'")
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>', self.print_contents)
        self.entrythingy.bind("<k>", self.turnRed)

    def turnRed(self, event):
        event.widget["fg"] = "red"


    def print_contents(self, event):
        print "hi. contents of entry is now ---->", self.contents.get()
        if self.contents.get().lower() == "options":
            self.createWidgets()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        #self.createWidgets()
        self.createEntrythingy()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
