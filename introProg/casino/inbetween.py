from random import *

def InBetween(balance):
    x = raw_input("Press ENTER to play, or enter any other key for directions.  ")
    if x != "": print "\n\nThis game is called In Between.\n\nFirst the player bets a portion of your balance to either be won or lost.\nThen, two random numbers are generated between 1 and 13, and are unknown to the player.\nThe player enters a number that they belive is between the two guessed.\nIf it is IN BETWEEN the two, your bet is added to your balance!\nIf it is not, or if it is one of the numbers generated, you lose your bet.\n\n"
    f,s,bet = randint(1,13),randint(1,13),0
    while bet < 5 or bet > balance:
        bet,guess = input("Enter your bet (minimum of 5),then guess (1-13) (ex. 10,7)\n>>> ")
    if f > s:
        a,b = s,f
    elif s > f:
        a,b = f,s
    if a<guess<b:
        print "You Win!"
    else:
        print "You lose..."
        bet -= bet*2
    print "The numbers were",a,"and",b,"."
    balance += bet
    return balance
