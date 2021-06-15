Height = int(input("Please determine a height of your pyramid : "))
for i in range(Height):
    print(" "*(Height - (1+i)),end = "")
    text = "*"*(i+1) + "*"*i
    print(text)