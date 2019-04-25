from inbetween import *
from guessinggame import *

def main():
    print "Welcome to Will and Ben's project."
    balance = input("What would you like your starting balance to be?\n>>> ")
    while balance != 0:
        print "\nYour balance is",balance
        choice = raw_input("Would you like to play:\n\n1) A Guessing Game\n2) Bennnn...\n3) In Between\n\n>>> ")
        if choice == "1":
            balance = guessinggame(balance)
        elif choice == "2":
            print "not yet..."#ben put your thing here
        if choice == "3":
            balance = InBetween(balance)
    print "Looks like you're all out of money..."

main()
