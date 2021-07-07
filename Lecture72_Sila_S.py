menuList = []
totalPrice = []
def showbill() :
    print("Summary".center(21,"-"))
    for number in range(len(menuList)) :
        print(f"{number+1}.", menuList[number][0], menuList[number][1],"Baht")
        totalPrice.append(menuList[number][1])
    print(f"Total {sum(totalPrice)} Baht")
    print("-".center(21,"-"))

while True :
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit" :
        break
    else :
        menuPrice = int(input("Price : "))
        menuList.append([menuName, menuPrice])

showbill()