menuList = []
priceList = []
def showbill() :
    print("Summary".center(21,"-"))
    for number in range(len(menuList)) :
        print(f"{number+1}.", menuList[number], priceList[number], "Baht")
    print("\nTotal", sum(priceList), "Baht")
    print("-".center(21,"-"))

while True :
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit" :
        break
    else :
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showbill()