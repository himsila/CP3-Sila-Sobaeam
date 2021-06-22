#Seperate problems into function
def Login() :
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "123456" :
        return True
    else :
        return False

def Menu() :
    print("------- Menu -------")
    print("1.Vat Calculator.")
    print("2.Sum Price Calculator.")
    choice = input("Selet program >>> ")
    return choice

def VatCalculator(totalPrice) :
    totalVat = totalPrice + (totalPrice * 0.07)
    return totalVat

def SumPriceCalculator() :
    price1 = int(input("1st Price : "))
    price2 = int(input("2nd Price : "))
    return VatCalculator(price1 + price2)


#------ Program -----
Ans = Login()
if Ans == True :
    userSelect = Menu()
    if userSelect == "1" :
        print("------- Vat Calculator -------")
        price = int(input("Input price : "))
        print("Total Price (Vat Included.) = ", VatCalculator(price))
    elif userSelect == "2" :
        print("------- Sum Price Calculator -------")
        print("Total Price (Vat Included.) = ", SumPriceCalculator())
    else :
        pass
else :
    pass
print("Done.")