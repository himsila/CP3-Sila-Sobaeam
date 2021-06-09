'''Determine a username and password.'''
strUsername = "customer"
strPassword = "123456"
Username = ""
Password = ""
i = 0
'''Section 1 : Select a menu.'''
print("------------- Log in -------------")
while Username != strUsername and Password != strPassword :
        Username = input("Username : ")
        Password = input("Password : ")
        if Username == strUsername and Password == strPassword :
            print("--- Welcome to abc shop ---")
            print("Select a menu...")
            print("1.Kraprao Kai    60 THB")
            print("2.Kraprao Mhoo   70 THB")
            print("3.Kraprao Thaley 80 THB")
            strMenuNo = input("Insert a menu number (1,2 or 3) >>>")

            '''Determine a menu and price.'''
            if strMenuNo == "1" :
                strMenu = "Krapro Kai"
                intPrice = 60
                x = 1
            elif strMenuNo == "2" :
                strMenu = "Krapro Mhoo"
                intPrice = 70
                x = 1
            elif strMenuNo == "3" :
                strMenu = "Krapro Thaley"
                intPrice = 80
                x = 1
            else :
                print("There's not in the menu!, Get out!")
                x = 0
        else :
            print("Username and password doesn't match.")
            x = 0

        '''Section 2 : Price summary.'''
        if x == 1 :
            print("Your seleted menu is", strMenu, ". How many dishes you would like to take?")
            n = int(input(">>> "))
            '''Calculate a total price + vat.'''
            if n >= 1 :
                intTotal = intPrice * n
                fltVat = intTotal * 0.07
                fltGrandTotal = intTotal + fltVat
                print("----------------------------------------")
                print("Total = ", intTotal, " THB")
                print("Vat 7% = ", fltVat, " THB")
                print("Grand Total = ", fltGrandTotal, " THB.")
                print("---------- Thank you. -----------")
            else :
                print("Are you kidding me? Get the f**k out of my face!!!")
        else :
            pass
print("Done.")