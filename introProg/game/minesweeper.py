import random
import time

#MAKE SURE to create a folder in the same directory as this file called "Users"

def avg(something):
    total = 0
    for i in something: total += int(i)
    return total/len(something)

class game(object):       #there will only be one instance of the class, that will be the game

    def __init__(self,gridsize,mines):
        self.mines,self.gridsize = mines,gridsize           #number of mines
        self.make_realgrid()         #this is the grid with all the bombs marked
        self.visgrid = [['+' for i in range(self.gridsize)] for i in range(self.gridsize)]
        self.guessed,self.curguess,self.mguessed,self.marked,self.bmarked,self.lost,self.won,self.guess_type = [],[],[],0,0,False,False,''
        self.gmain()


    def make_realgrid(self):   #this will make the grid with the bombs
        bomblist = []           #this list is the list of bombs I've made
        self.real_grid = [['+' for i in range(self.gridsize)] for i in range(self.gridsize)]      #a list of those rows
        for i in range(self.mines):                     #this loop generates all of the x,y coordinates of bombs
            while len(bomblist) == i:
                x = random.randint(0,self.gridsize-1)
                y = random.randint(0,self.gridsize-1)
                if not ([x,y] in bomblist):
                    self.real_grid[y][x] = '@'                  #then the loop marks them with a '@'
                    bomblist.append([x,y])

    def display_grid(self,grid):
        rowtoprint = ''                                          #this is the corner piece in the top left
        for c in [' x '] + [i for i in range(self.gridsize)]: rowtoprint += str(c)    #Generate the top row of digits with a space on the left
        print rowtoprint + "\ny"
        for rownum in range(len(grid)):             #repeat by row
            rowtoprint = str(rownum) + '  '                  #the row number
            for b in (grid[rownum]): rowtoprint += str(b)
            print rowtoprint                                #after reading through my code I have determined that you should just trust this function, it works

    def takeguess(self):            #why didnt we comment this
        repeat = True
        print "Do want to Mark, Unmark, or Clear a tile?\nYou must enter (m/u/c)."
        while repeat == True:
            self.guess_type = raw_input(">>> ")
            if self.guess_type == "m" or self.guess_type == "u" or self.guess_type == "c":
                guess = [input("x coordinate?\n>>> "),input("y coordinate?\n>>> ")]
                while (guess in self.guessed) or guess[0] > self.gridsize - 1 or guess[1] > self.gridsize - 1 or guess[0] < 0 or guess[1] < 0:
                    print "\nPlease enter valid coordinates.\n"
                    guess = [input("x coordinate?\n>>> "),input("y coordinate?\n>>> ")]
                self.curguess = guess
                if self.guess_type == 'c': self.guessed.append(self.curguess)
                elif self.guess_type == 'm': self.mguessed.append(self.curguess)
                repeat = False
            else: print "You MUST enter m, u, or c."

    def nearmines(self,x,y):     #working, high quality function that calculates the mines near a tile
        adjacent = 0
        for ty in range(y-1,y+2):
            for tx in range (x-1,x+2):
                try:
                    if -1 in [tx,ty]: continue
                    if self.real_grid[ty][tx] == '@': adjacent += 1
                except IndexError: pass
        return adjacent

    def zero_clear(self,x,y):       #the fuction the recurses around a zero tile when you guess it
        for tx in range(x-1,x+2):
            for ty in range(y-1,y+2):   #iterates through the tiles around the one you guessed
                if (not ([tx,ty] in self.guessed)) and not (-1 in [tx,ty]) and (tx < self.gridsize) and (ty < self.gridsize):     #if it's not -1 (cuz that's some errors) and it's not already guessed also checks if it won't give a list index error
                        self.curguess = [tx,ty]         #so update_visgrid knows we are guessing it
                        self.guessed.append([tx,ty])    #so we won't accidentally guess it again
                        self.update_visgrid()           #now update the visgrid :)

    def update_visgrid(self):
        x = self.curguess[0]
        y = self.curguess[1]
        if self.guess_type == 'c':
            try:
                if self.real_grid[y][x] == '@': self.lost = True
                else:
                    self.visgrid[y][x] = self.nearmines(x,y)       #now actualy put it in
                    self.real_grid[y][x] = self.nearmines(x,y)
                    if self.nearmines(x,y) == 0: self.zero_clear(x,y)
            except IndexError: print "This is embarassing... I failed finding",x,y
        elif self.guess_type == 'm':
            if self.real_grid[y][x] == '@': self.marked += 1
            else: self.bmarked += 1
            self.visgrid[y][x] = '@'
            if (self.marked == self.mines) and (self.bmarked == 0): self.won = True
        elif self.guess_type == 'u':
            if self.real_grid[y][x] == '@': self.marked -= 1
            else: self.bmarked -= 1
            self.visgrid[y][x] = '+'
            self.mguessed.remove([x,y])

    def gmain(self):
        while self.won != True and self.lost != True:
            self.display_grid(self.visgrid)      #displays the visible grid
            self.takeguess()            #takes the user input for their guess
            self.update_visgrid()       #updates the visible grid based on their guess
        if self.lost:                   #if they lost say they lost
            print "You hit a mine...\nThis is where all the mines were:\n"
            self.display_grid(self.real_grid)
            win = False
        elif self.won:
            print "\nYou Win!\n"
            win = True
        global marked
        marked = self.marked

#WILL COMMENTED THE NEXT TWO FUNCTIONS BTW

def getscores(filename):
    try:                            #try to read a pre-existing file
        with open(filename,"r") as file:
            lines = file.readlines()       #exact lines of the file
            all_scores = [[],[],[],[]]  #item 0 will be easy, item 1 med, item  2 hard, item 3 custom
            base_scores = []            #this list is necessary to complete all_scores
            for line in lines: base_scores.append(''.join(i for i in line if i != "\n"))   #removes any \n's (very pythonic)
            for i in range(0,4):                        #this loop adds each number as an integer to all_scores
                for b in base_scores[i].split(" "):     #split each string in base_scores into a list of strings
                    if b.isdigit(): all_scores[i].append(b)        #turn those str's into int's and add them to all_scores
            return all_scores                           #return all 4 categories of scores
    except (IOError, IndexError):                 #create a new file INSTEAD of reading one
        with open(filename,"w") as file:          #open the file to write
            for i in range(0,4): file.write("\n") #write four empty lines
            return [[],[],[],[]]    #no scores, no items

def savescore(filename,score,game_mode):
    scores = getscores(filename)    #get the lists of scores so that we can add to them
    with open(filename,"w") as file:       #in write mode:
        file.truncate()                    #clear the file
        scores[game_mode-1].append(score)  #add the current score to the corresponding list
        for i in scores: file.write(" ".join(str(i))+"\n") #repeat for each line and write those lists (as strings) to the file


def main():
    keep_playing = "y"
    username = raw_input("Welcome to Minesweeper!\n\nPlease enter your username: ")
    filename = "Users/"+username
    while keep_playing == "y":
        scores = getscores(filename)
        if scores == [[],[],[],[]]:
            print "Welcome New User: %s!\n\nYou have no previous scores." %(username)
            scores = [[""],[""],[""],[""]]
        else:
            for i in scores:
                for a in i:
                    if a.isdigit() == False: scores[scores.index(i)][scores[i].index(a)] = ""
            print "Welcome back, %s!\nHere are you previous scores:\nEasy Difficulty:  " %(username),scores[0],"\nMedium Difficulty:",scores[1],"\nHard Difficulty:  ",scores[2],"\nCustom Game:      ",scores[3]
        begin = raw_input("Would you like to begin? ")
        game_mode = input("What difficulty would you like to play on?\n\n1. Easy\n2. Medium\n3. Hard\n4. Custom\n\n>>> ")
        if   game_mode == 1: mygame,mode = game(5,7),"Easy Mode"
        elif game_mode == 2: mygame,mode = game(7,15),"Medium Mode"
        elif game_mode == 3: mygame,mode = game(10,35),"Hard Mode"
        elif game_mode == 4:
            gridsize = input("How big should the grid be? (squared)\n>>> ")
            mygame,mode = game(gridsize,input("How many mines should there be on the grid? (There cannot be more than %d)\n>>> " %(gridsize*gridsize))),"Custom Mode"
        savescore(filename,marked,game_mode)
        scores = getscores(filename)
        print "Nice Job! Your score was",marked,"\nYour high score on",mode,"is:",max(scores[game_mode-1]),"\nYour average score is now",avg(scores[game_mode-1])
        keep_playing = raw_input("\nWould you like to keep playing? (y/n)\n>>> ")
    print "Thanks for playing!"

if __name__ == "__main__":
    main()
