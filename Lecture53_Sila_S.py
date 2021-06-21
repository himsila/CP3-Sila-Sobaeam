def calVAT(x) :
    vat = x * 0.07
    vatTotal = x + vat
    return vatTotal
#------- Program ----------
price = int(input("Input price : "))
print(f"Price (Vat Included) = {calVAT(price)}")