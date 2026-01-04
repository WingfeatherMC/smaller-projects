answer1 = input("Welcome to the Unofficial Call Of Duty Camo Tracker! Type 'y' to start!") #starting line
print ("Please type all names as they appear to avoid error messages, e.g. 'Lachmann Sub', not 'lachmann sub'. Thanks in advance! ")
if answer1 in ["y","Y"]:
    cat1 = input("What gun category do you want to track camo for? (SMG, AR, or Sniper):") #Choose category
    if cat1 in ["SMG","Smg","smg"]:
        smg1 = input("Which SMG do you want to do? (Lachmann sub, Vel 46, BAS-P):") #choose which smg
        if smg1 in ["Lachmann sub","Lachmann","lachmann sub","Lachmann Sub","lachmann"]:
            print ("You chose the Lachmann Sub!")
            killsLMNS = 0
            while killsLMNS < 50:
                kills1LMNS = int(input("How many kills this match?"))
                if kills1LMNS < 0:
                    print ("Invalid Number")
                    print (str(killsLMNS) + " is the number of current total kills")#error contingency
                    continue
                killsLMNS = killsLMNS + kills1LMNS #kill tracking printout
                print (str(killsLMNS) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        elif smg1 in ["Vel 46","vel 46","vel46"]:
            print ("You chose the Vel 46!")
            killsVEL = 0
            while killsVEL < 50:
                kills1VEL = int(input("How many kills this match?"))
                if kills1VEL < 0:
                    print ("Invalid Number")
                    print (str(killsVEL) + " is the number of current total kills")#error contingency
                    continue
                killsVEL = killsVEL + kills1VEL #kill tracking printout
                print (str(killsVEL) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        elif smg1 in ["BASP","BAS-P","BAS-p","basp"]:
            print ("You chose the BAS-P!")
            killsBASP = 0
            while killsBASP < 50:
                kills1BASP = int(input("How many kills this match?"))
                if kills1BASP < 0:
                    print ("Invalid Number")
                    print (str(killsBASP) + " is the number of current total kills")#error contingency
                    continue
                killsBASP = killsBASP + kills1BASP #kill tracking printout
                print (str(killsBASP) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        
    if cat1 in ["AR","Ar","aR","ar"]:
        ar1 = input("Which AR do you want to do? (M4, M13b, ISO Hemlock):") #choose which ar
        if ar1 in ["M4","m4"]:
            print ("You chose the M4!")
            killsM4 = 0
            while killsM4 < 50:
                kills1M4 = int(input("How many kills this match?"))
                if kills1M4 < 0:
                    print ("Invalid Number")
                    print (str(killsM4) + " is the number of current total kills")
                    continue
                killsM4 = killsM4 + kills1M4 #kill tracking loop
                print (str(killsM4) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        if ar1 in ["M13b","m13B","M13B","m13b"]:
            print ("You chose the M13B!")
            killsM13B = 0
            while killsM13B < 50:
                kills1M13B = int(input("How many kills this match?"))
                if kills1M13B < 0:
                    print ("Invalid Number")
                    print (str(killsM13B) + " is the number of current total kills")
                    continue
                killsM13B = killsM13B + kills1M13B #kill tracking loop
                print (str(killsM13B) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        if ar1 in ["ISOH","Iso Hemlock","ISO Hemlock","iso hemlock"]:
            print ("You chose the ISO Hemlock!")
            killsISOH = 0
            while killsISOH < 50:
                kills1ISOH = int(input("How many kills this match?"))
                if kills1ISOH < 0:
                    print ("Invalid Number")
                    print (str(killsISOH) + " is the number of current total kills")
                    continue
                killsISOH = killsISOH + kills1ISOH #kill tracking loop
                print (str(killsISOH) + " is the number of current total kills")
            print ("Congratulations on your camo!")
    if cat1 in ["Sniper","sniper","SNIPER"]:
        spr1 = input("Which sniper rifle do you want to do? (LA-B 330, Victus XMR, SP-X 80):") #choose which sniper
        if spr1 in ["LA-B 330","LAB 330","lab 330"]:
            print ("You chose the LA-B 330!")
            killsLAB330 = 0
            while killsLAB330 < 50:
                kills1LAB330 = int(input("How many kills this match?"))
                if kills1LAB330 < 0:
                    print ("Invalid Number")
                    print (str(killsLAB330) + " is the number of current total kills")
                    continue
                killsLAB330 = killsLAB330 + kills1LAB330 #kill tracking loop
                print (str(killsLAB330) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        if spr1 in ["XMR","Victus XMR","victus","victus xmr","Victus"]:
            print ("You chose the Victus XMR!")
            killsXMR = 0
            while killsXMR < 50:
                kills1XMR = int(input("How many kills this match?"))
                if kills1XMR < 0:
                    print ("Invalid Number")
                    print (str(killsXMR) + " is the number of current total kills")
                    continue
                killsXMR = killsXMR + kills1XMR #kill tracking loop
                print (str(killsXMR) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        if spr1 in ["SP-X 80","SPX 80","sp-x 80","spx80"]:
            print ("You chose the SP-X 80!")
            killsSPX = 0
            while killsSPX < 50:
                kills1SPX = int(input("How many kills this match?"))
                if kills1SPX < 0:
                    print ("Invalid Number")
                    print (str(killsSPX) + " is the number of current total kills")
                    continue
                killsSPX = killsSPX + kills1SPX #kill tracking loop
                print (str(killsSPX) + " is the number of current total kills")
            print ("Congratulations on your camo!")
        
