print("Height Calculator")
foot = int(input("Foots: "))
inches = float(input("Inches: "))

x = (foot*30 + inches*2.54)
y = x / 100
print("Your height is: "+str(x)+" cm "+"or "+str(y)+" m")

