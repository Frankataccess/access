#weight converter

weight = float(input("please enter your weight:"))
unit = input("(K)g or (L)bs: ")
unit = unit.upper()
if unit == "K":
    weight = weight * 2.2046226218
    print(weight,"Lbs")
elif unit == "L":
    weight = weight * 0.45359237
    print(weight,"Kg")
else:
    print ("invalid choice!")