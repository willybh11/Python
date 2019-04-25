from Tkinter import *

class Game(Frame):


    def setup(self):
        self.nums = [[],[],[],[]]
        for i in range(4):
            for j in range(4):
                self.nums[i].append("--")

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master.title("2048")
        self.grid()
        self.setup()
        self.drawGrid()

    def drawDirectionButtons(self):
        self.LEFT = Button(self)
        self.LEFT["text"] = "<-"
        self.LEFT["command"] = self.doNothing
        self.LEFT.grid(row=8,column=4,rowspan=2,columnspan=2,sticky=N+E+S+W)

    def drawGrid(self):
        self.TL = Button(self)
        self.TL["text"] = "\n   "+self.nums[0][0]+"   \n"
        self.TL["command"] = self.doNothing
        self.TL.grid(row=0,column=0,rowspan=2,columnspan=2,sticky=N+E+S+W)

        self.TML = Button(self)
        self.TML["text"] = "\n   "+self.nums[0][1]+"   \n"
        self.TML["command"] = self.doNothing
        self.TML.grid(row=0,column=2,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.TMR = Button(self)
        self.TMR["text"] = "\n   "+self.nums[0][2]+"   \n"
        self.TMR["command"] = self.doNothing
        self.TMR.grid(row=0,column=4,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.TR = Button(self)
        self.TR["text"] = "\n   "+self.nums[0][3]+"   \n"
        self.TR["command"] = self.doNothing
        self.TR.grid(row=0,column=6,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MTL = Button(self)
        self.MTL["text"] = "\n   "+self.nums[1][0]+"   \n"
        self.MTL["command"] = self.doNothing
        self.MTL.grid(row=2,column=0,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MTML = Button(self)
        self.MTML["text"] = "\n   "+self.nums[1][1]+"   \n"
        self.MTML["command"] = self.doNothing
        self.MTML.grid(row=2,column=2,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MTMR = Button(self)
        self.MTMR["text"] = "\n   "+self.nums[1][2]+"   \n"
        self.MTMR["command"] = self.doNothing
        self.MTMR.grid(row=2,column=4,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MTR = Button(self)
        self.MTR["text"] = "\n   "+self.nums[1][3]+"   \n"
        self.MTR["command"] = self.doNothing
        self.MTR.grid(row=2,column=6,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MBL = Button(self)
        self.MBL["text"] = "\n   "+self.nums[2][0]+"   \n"
        self.MBL["command"] = self.doNothing
        self.MBL.grid(row=4,column=0,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MBML = Button(self)
        self.MBML["text"] = "\n   "+self.nums[2][1]+"   \n"
        self.MBML["command"] = self.doNothing
        self.MBML.grid(row=4,column=2,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MBMR = Button(self)
        self.MBMR["text"] = "\n   "+self.nums[2][2]+"   \n"
        self.MBMR["command"] = self.doNothing
        self.MBMR.grid(row=4,column=4,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.MBR = Button(self)
        self.MBR["text"] = "\n   "+self.nums[2][3]+"   \n"
        self.MBR["command"] = self.doNothing
        self.MBR.grid(row=4,column=6,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.BL = Button(self)
        self.BL["text"] = "\n   "+self.nums[3][0]+"   \n"
        self.BL["command"] = self.doNothing
        self.BL.grid(row=6,column=0,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.BML = Button(self)
        self.BML["text"] = "\n   "+self.nums[3][1]+"   \n"
        self.BML["command"] = self.doNothing
        self.BML.grid(row=6,column=2,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.BMR = Button(self)
        self.BMR["text"] = "\n   "+self.nums[3][2]+"   \n"
        self.BMR["command"] = self.doNothing
        self.BMR.grid(row=6,column=4,rowspan=2,columnspan=2)#,sticky=N+E+S+W)

        self.BR = Button(self)
        self.BR["text"] = "\n   "+self.nums[3][3]+"   \n"
        self.BR["command"] = self.doNothing
        self.BR.grid(row=6,column=6,rowspan=2,columnspan=2)#,sticky=N+E+S+W)


    def doNothing(self):
        pass



root = Tk()
app = Game(master=root)
app.mainloop()
root.destroy()
