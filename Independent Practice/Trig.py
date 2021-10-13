import math as m
radius = input("Give me an angle, and whether it is in degrees or radians separated by a space, and I will output the subsequent sin, cos, and tan.\n").split(" ")
number = 0
degrad = ""
for i in range(0, len(radius)):
    try:
        number = float(radius[i])
    except:
        degrad = radius[i]
if degrad[0].upper() == "D":
    radians = m.radians(number)
    print("Sine:", m.sin(radians),"\nCosine:", m.cos(radians),"\nTangent:", m.tan(radians))
else:
    radians = number
    print("Sine:", m.sin(radians),"\nCosine:", m.cos(radians),"\nTangent:", m.tan(radians))