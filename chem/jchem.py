def comblaw():
    s=""
    while s == "":
        x=raw_input('Solve for "P" "V" "N" or "T":')
        if x in "PVNT":
            s="o"
    P1,P2,V1,V2,c,g,T1,T2="","","","","","","","",
    print "Enter numbers with their unit seperated by a space e.g. 273.15 K \nPlease enter units as such (atm, kPa, mmHg, mL, L, C, K)\nN1 and N2 don't need units\nWhatever unit is put on the variable you are solving for will be the unit of the answer"
    while P1 == "":
        a=raw_input("P1:")
        P1=check(a,a,"","P")
    while V1 == "":
        b=raw_input("V1:")
        V1=check(b,b,"","V")
    while isinstance(c, float) == False:
        c=input("N1:")*1.0
    while T1 == "":
        d=raw_input("T1:")
        T1=check(d,d,"","T")
    while P2 == "":
        e=raw_input("P2:")
        P2=check(e,a,e,"P")
    while V2 == "":
        f=raw_input("V2:")
        V2=check(f,b,f,"V")
    while isinstance(g, float) == False:
        g=input("N2:")*1.0
    while T2 == "":
        h=raw_input("T2:")
        T2=check(h,d,h,"T")
    if x=="P":
        ans=str(((g*T2)*(P1*V1))/((c*T1)*(V2)))+" atm"
        ans=str(check(ans,e,ans,"P"))+e[e.index(" ")+1:]
    if x=="V":
        ans=str(((g*T2)*(P1*V1))/((c*T1)*(P2)))+" L"
        ans=str(check(ans,f,ans,"V"))+f[f.index(" ")+1:]
    if x=="N":
        ans=str(((P2*V2)*(c*T1))/((P1*V1)*(T2)))+"mol"
    if x=="T":
        ans=str(((P2*V2)*(c*T1))/((P1*V1)*(g)))+" K"
        ans=str(check(ans,h,ans,"TF"))+" "+h[h.index(" ")+1:]
    print ans,"\n"
    return

def check(a,one,two,u):
    if " " in a and a[0:a.index(" ")] !="" and a[a.index(" ")+1:] != "":
        au=a[a.index(" ")+1:]
        if u=="P" and au not in ("atm", "mmHg", "kPa"):
            print "Wrong unit"
        elif u=="V" and au not in ("mL","L"):
            print "Wrong unit"
        elif u=="T" and au not in ("C", "K"):
            print "Wrong unit"
        else:
            oneu=one[one.index(" ")+1:]
            twou=two[two.index(" ")+1:]
            twon=eval(two[0:two.index(" ")])
            if "T" in u:
                if au== "C":
                    ans=eval(a[0:a.index(" ")])+273.15
                if u=="TF" and twou=="C":
                    ans=twon-273.15
                else:
                    ans=eval(a[0:a.index(" ")])
            elif two != "" and oneu != two[two.index(" ")+1:]:
                if u=="P":
                    if oneu== "atm":
                        if twou== "mmHg":
                            ans=twon/760
                        else:
                            ans=twon/101.325
                    if oneu== "mmHg":
                        if twou== "atm":
                            ans=twon*760
                        else:
                            ans=twon*(760/101.325)
                    if oneu== "kPa":
                        if twou== "mmHg":
                            ans=twon*(101.325/760)
                        else:
                            ans=twon*101.325
                if u=="V":
                    if oneu== "mL":
                        ans=twon*1000
                    else:
                        ans=twon/1000
            else:
                ans=eval(a[0:a.index(" ")])
            return ans*1.0
    return ""
def main():
    while True:
        comblaw()
main()
