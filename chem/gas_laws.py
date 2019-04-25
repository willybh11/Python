def takeinput(c):
    P,V,n,T = {"P1":raw_input("P1: ").split()},{"V1":raw_input("V1: ").split()},{"n1":raw_input("n1: ").split()},{"T1":raw_input("T1: ").split()}
    if c == 1: P["P2"],V["V2"],n["n2"],T["T2"] = raw_input("\nP2: ").split(),raw_input("V2: ").split(),raw_input("n2: ").split(),raw_input("T2: ").split()
    return [P,V,n,T] #the above line adds a second valueset (for combined gas law)
def convert(var,c):
    for a in var:       #a is the variable in question
        for b in a:     #b is the key of the dict (of each indiv variable)
            if a[b] != [] and a[b][0] != '1':    #check for undefined variables
                if a[b][1] == "F":   a[b][0] = (float(a[b][0]) + 459.67) * (5/9);               print "**Farenheit value converted to Kelvin."
                if a[b][1] == "C":   a[b][0] = float(a[b][0]) + 273.15;                         print "** Celsius value converted to Kelvin."
                if a[b][1] == "mL":  a[b][0] = float(a[b][0]) / 1000;                           print "** mL value converted to L."
                if c == 1:  #convert variables specific to the combined gas law
                    if a[b][1] == "atm": a[b][0] = float(a[b][0]) * 101.325;                    print "** ATM value converted to kPa."
                    if a[b][1] in ["mmHg","torr"]: a[b][0] = float(a[b][0]) * 7.5006156130264;  print "** mmHg/torr value converted to kPa."
                else:       #convert variables specific to the ideal gas law
                    if a[b][1] == "kPa": a[b][0] = float(a[b][0]) * 0.00986923;                 print "** kPa value converted to ATM."
                    if a[b][1] in ["mmHg","torr"]: a[b][0] = float(a[b][0]) / 760;              print "** mmHg/torr value converted to ATM."
    return var      #[var] is now converted to equation specific units
def equation(var,c):
    P,V,n,T,R = var[0],var[1],var[2],var[3],0.082057
    if c == 1:  #solve for combined gas law
        if P["P2"] == []: return [ "You solved for P2 and got:", ( float(P["P1"][0]) * float(V["V1"][0]) * float(n["n2"][0]) * float(T["T2"][0]) ) / ( float(n["n1"][0]) * float(T["T1"][0]) * float(V["V2"][0]) ) , "kPa"]
        if V["V2"] == []: return [ "You solved for V2 and got:", ( float(P["P1"][0]) * float(V["V1"][0]) * float(n["n2"][0]) * float(T["T2"][0]) ) / ( float(n["n1"][0]) * float(T["T1"][0]) * float(P["P2"][0]) ) , "L"  ]
        if n["n2"] == []: return [ "You solved for n2 and got:", ( float(P["P2"][0]) * float(V["V2"][0]) * float(n["n1"][0]) * float(T["T1"][0]) ) / ( float(T["T2"][0]) * float(P["P1"][0]) * float(V["V1"][0]) ) , "mol"]
        if T["T2"] == []: return [ "You solved for T2 and got:", ( float(P["P2"][0]) * float(V["V2"][0]) * float(n["n1"][0]) * float(T["T1"][0]) ) / ( float(P["P1"][0]) * float(V["V1"][0]) * float(n["n2"][0]) ) , "K"  ]
    else:       #solve for ideal gas law
        if P["P1"] == []: return [ "You solved for P and got:", ( ( float(n["n1"][0]) * float(T["T1"][0]) * R) / float(V["V1"][0]) )  , "atm" ]
        if V["V1"] == []: return [ "You solved for V and got:", ( ( float(n["n1"][0]) * float(T["T1"][0]) * R) / float(P["P1"][0]) )  , "L"   ]
        if n["n1"] == []: return [ "You solved for n and got:", ( ( float(P["P1"][0]) * float(V["V1"][0]) ) / ( R * float(T["T1"][0]) ) ), "mol" ]
        if T["T1"] == []: return [ "You solved for T and got:", ( ( float(P["P1"][0]) * float(V["V1"][0]) ) / ( R * float(n["n1"][0]) ) ), "K"   ]
if __name__ == "__main__":
    c = input("1)  Combined Gas Law\n2)  Ideal Gas Law\n>>> ")  #choose law
    solution = equation(convert(takeinput(c),c),c)  #main
    print solution[0],solution[1],solution[2]       #print pre-determined string
