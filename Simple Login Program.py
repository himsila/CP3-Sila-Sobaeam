strUsername = input("Username :")
strPassword = input("Password :")
if strUsername == "admin" and strPassword == "1234":
    print("Logged in.")
    print("------ Select Program ------")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    strSelected = input("Insert program number >>> ")
    if strSelected == "1":
        print("------ Vat Calculator ------")
        fltPdPrice = float(input("Price :"))
        fltPdVat = fltPdPrice * 0.07
        print("Vat 7% = ", fltPdVat, "THB")
        print("Done.")
    elif strSelected == "2":
        print("------ Price Calculator ------")
        intPdPrice1 = int(input("Price-1 :"))
        intPdPrice2 = int(input("Price-2 :"))
        intTotal = intPdPrice1 + intPdPrice2
        print("Total =", intTotal, "THB")
        print("Done.")
    else:
        print("You insert wrong number.")
else:
    print("Username and Password doesn't match.")