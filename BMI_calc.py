print("BMI Calculator")
foot = int(input("Foots: "))
inches = float(input("Inches: "))
mass = float(input("Weight: "))

x = (foot*30 + inches*2.54)
y = x / 100
z = mass / (y*y)

print("Your BMI is: "+str(z))
