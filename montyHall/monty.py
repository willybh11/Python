# Simulating the Monty Hall problem
import random

def playGame(initial,action,doors,totWins):
    placed = random.choice(doors)  # Prize placed randomly
    chosen = initial               # Your first choice
    used   = [chosen,placed]       # Moderator chooses an empty door
    opened = random.choice([door for door in doors if door not in used])
    if action == "S" : chosen = switchDoor(doors,chosen,opened)
    youWin = (chosen == placed)
    if youWin : totWins += 1
    printInfo(placed,initial,opened,chosen,totWins,action,youWin)
    return totWins

def printInfo(placed,initial,opened,chosen,totWins,action,youWin):
    print "  Prize placed behind door %s"                   %(placed),
    print "-You chose %s -Moderator opened door %s"         %(initial,opened),
    if action == "H" : print  "-You held to %s"             %(chosen),
    if action == "S" : print  "-You switched to %s"         %(chosen),
    if youWin        : print  "-You win (wins now %i)"      %(totWins),
    print

def switchDoor(doors,chosen,opened):
    avail  = [door for door in doors if door not in [chosen,opened]]
    return avail[0]          # should be the only door left

def main():
    initial = raw_input("Initial choice (A,B,C)? ").upper()
    action  = raw_input("Always Switch/Hold (S,H) ? ").upper()
    doors   = ["A","B","C"]
    totWins = 0
    for i in range(100):
        totWins = playGame(initial,action,doors,totWins)
    print "\n\n\nWin Percentage: %i" %(totWins)

main()