c,P,V,n,T,R=input("1)  Combined Gas Law\n2)  Ideal Gas Law\n>>> "),{"P1":raw_input("P1: ").split()},{"V1":raw_input("V1: ").split()},{"n1":raw_input("n1: ").split()},{"T1":raw_input("T1: ").split()},0.082057
if c == 1:P["P2"],V["V2"],n["n2"],T["T2"]=raw_input("\nP2: ").split(),raw_input("V2: ").split(),raw_input("n2: ").split(),raw_input("T2: ").split()
for a in [P,V,n,T]:
    for b in a:
        if a[b]!=[] and a[b][0]!='1':
            if a[b][1]=="F":a[b][0]=(float(a[b][0])+459.67)*(5/9)
            if a[b][1]=="C":a[b][0]=float(a[b][0])+273.15
            if a[b][1]=="mL":a[b][0]=float(a[b][0])/1000
            if c==1:
                if a[b][1]=="atm":a[b][0]=float(a[b][0])*101.325
                if a[b][1]in["mmHg","torr"]:a[b][0] = float(a[b][0])*7.5006156130264
            else:
                if a[b][1]=="kPa":a[b][0]=float(a[b][0])*0.00986923
                if a[b][1]in["mmHg","torr"]:a[b][0]=float(a[b][0])/760
if c == 1:
    if P["P2"]==[]:print["You solved for P2 and got:",(float(P["P1"][0])*float(V["V1"][0])*float(n["n2"][0])*float(T["T2"][0]))/(float(n["n1"][0])*float(T["T1"][0])*float(V["V2"][0])),"kPa"]
    if V["V2"]==[]:print["You solved for V2 and got:",(float(P["P1"][0])*float(V["V1"][0])*float(n["n2"][0])*float(T["T2"][0]))/(float(n["n1"][0])*float(T["T1"][0])*float(P["P2"][0])),"L"]
    if n["n2"]==[]:print["You solved for n2 and got:",(float(P["P2"][0])*float(V["V2"][0])*float(n["n1"][0])*float(T["T1"][0]))/(float(T["T2"][0])*float(P["P1"][0])*float(V["V1"][0])),"mol"]
    if T["T2"]==[]:print["You solved for T2 and got:",(float(P["P2"][0])*float(V["V2"][0])*float(n["n1"][0])*float(T["T1"][0]))/(float(P["P1"][0])*float(V["V1"][0])*float(n["n2"][0])),"K"]
else:
    if P["P1"]==[]:print["You solved for P and got:",((float(n["n1"][0])*float(T["T1"][0])*R)/float(V["V1"][0])),"atm"]
    if V["V1"]==[]:print["You solved for V and got:",((float(n["n1"][0])*float(T["T1"][0])*R)/float(P["P1"][0])),"L"]
    if n["n1"]==[]:print["You solved for n and got:",((float(P["P1"][0])*float(V["V1"][0]))/(R*float(T["T1"][0]))),"mol"]
    if T["T1"]==[]:print["You solved for T and got:",((float(P["P1"][0])*float(V["V1"][0]))/(R*float(n["n1"][0]))),"K"]
