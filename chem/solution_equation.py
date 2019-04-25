#
#     moles solute
#  -------------------     * 100     =   Molarity %
#  liter solution total
#

def main():
    print "Type in the value, and then the units.\n\nex. 340 mL\nex. 12 g\nex. 3.4 %\nex. 5 m\n\nLeave the unknown as 'x', and make sure to put the units after it.\n\nex. x g\n\nSupported units: L, mL, g, m, %.\n"
    raw = [raw_input("Amount of Solute: ").upper(),raw_input("Solution Total: ").upper(),raw_input("Molarity %: ").upper()]

def convert(raw):
    converted = []
    for x in raw:
        if x[-2:-1] == "ML":
            converted.append(x/1000)
        
