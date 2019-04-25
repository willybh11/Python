import os

class ToDo(object):
    def __init__(self):
        self.tdlist = {}
        self.title = 'useless text'
        self.plural = 'items'
        self.local = os.listdir(os.getcwd()+"/Lists")
        self.options = ['Add an Item','Remove an Item','Clear the List','Delete the List','Complete an Item','Revert an Item','Quit']
        self.functions = {'Add an Item': self.additem,'Remove an Item':self.remitem,'Clear the List':self.clearlist,'Delete the List':self.delfile,'Save Data to File':self.savefile,'Complete an Item':self.compitem,'Revert an Item':self.revitem,'Quit':self.exit}
        self.UI()

    def UI(self):

        print "Welcome to Will's ToDo Program!\n\nWhich list would you like to open?"

        for i in range(len(self.local)):
            print str(i+1)+")\t"+self.local[i]              #print local filenames

        try:        #try to find existing file
            self.title = self.local[input("Enter valid list number, or type 'new':\n>>> ")-1]
            self.getfile()
        except:     #if file does not exist:
            self.title = raw_input("What would you like your new list to be called?\n>>> ")
            self.savefile()

        while 1:    #loop until broken
            if len(self.tdlist) == 1: self.plural = 'item'    #change to correct grammar
            else: self.plural = 'items'
            print "\nIn %s you have %i %s:" %(self.title,len(self.tdlist),self.plural)   #print num of list items
            for i in self.tdlist:
                print i," "*(24-(len(i))),"-",self.tdlist[i]    #print list items

            print "\nWhat would you like to do?"                                #printed BEFORE list of functions
            for i in range(len(self.options)):
                print str(i+1)+")\t"+self.options[i]            #print functions

            choice = self.options[input(">>> ")-1]      #user input of function

            if choice != "Quit":            #If quit, UI ends here

                self.functions[choice]()    #run the chosen function

                if choice != 'Delete the List': #if the list is NOT to be deleted:
                    print 'You have chosen to %s in %s.' %(choice,self.title)
                    self.savefile()             #print what you have done, and save it
                else:   break       #if you chose to delete the list
            else:       break       #if you choose to quit the Program

        print "Thanks for using my ToDo program!"

    def exit(self):
        print 'Session Ended.'
        quit()


    def additem(self):          #user input NEW key, value will be incomplete
        self.tdlist[raw_input("\nEnter new item name: (try to keep it under 24 characters...)\n   |       <-- 24 -->       |\n>>> ")] = 'Incomplete.'
        print "Item added!"     

    def remitem(self):          #user input key, delete item
        del self.tdlist[raw_input("\nEnter the name of the item you would like to remove\n>>> ")]
        print "Item deleted!"   

    def compitem(self):         #user input key, change value to complete
        itemname = '123456'
        while itemname not in self.tdlist:
            itemname = raw_input("\nEnter valid item name to complete:\n>>> ")
        self.tdlist[itemname] = "Complete!"

    def revitem(self):          #user input key, change value to incomplete
        itemname = 'youwillneverenterthis'
        while itemname not in self.tdlist:
            itemname = raw_input("\nEnter valid item name to revert:\n>>> ")
        self.tdlist[itemname] = "Incomplete."

    def clearlist(self):        #remove all items from tdlist
        self.tdlist = {}
        print "List Cleared."

    def delfile(self):          #delete corresponding file (no user input needed)
        os.remove("Lists/"+self.title)
        print "List (file) Deleted."

    def savefile(self):         #save data to list-specific file
        with open("Lists/" + self.title,'w+') as f:     
            for i in self.tdlist: 
                f.write(i+"|"+self.tdlist[i]+"\n")  #write item|value per line to file

    def getfile(self):          #retrieve data from a list-specific file
        with open("Lists/" + self.title,"r") as f:
            for i in f.readlines():
                x = i.strip("\n").split("|")    #strip of newlines and split into list of [key, value]
                self.tdlist[x[0]] = x[1]        #set the list to an item in tdlist


if __name__ == "__main__":
    todo = ToDo()   #initiate class
