def Plus(x, y):
    print(f"{x} + {y} = {x + y}")
def Minus(x, y):
    print(f"{x} - {y} = {x - y}")
def Multiplying(x, y):
    print(f"{x} * {y} = {x * y}")
def Division(x, y):
    print(f"{x} / {y} = {int(x / y)}")

print("-------- Let's Cal! --------")
x = int(input("First number : "))
y = int(input("Second number : "))
print("-------- Results --------")
Plus(x, y)
Minus(x, y)
Multiplying(x, y)
Division(x, y)
print("Done.")