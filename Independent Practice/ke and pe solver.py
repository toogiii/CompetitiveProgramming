peke = input("GPE or KE\n").upper()
if peke == "GPE":
    mgh = input("m, g, h, or pe\n").lower()
    if mgh == "pe":
        m = int(input("mass\n"))
        g = int(input("gravity\n"))
        h = int(input("height\n"))
        print(m*g*h)
    elif mgh == "m":
        pe = int(input("potential energy\n"))
        g = int(input("gravity\n"))
        h = int(input("height\n"))
        print(pe/(g*h))
    elif mgh == "g":
        m = int(input("mass\n"))
        pe = int(input("potential energy\n"))
        h = int(input("height\n"))
        print(pe/(h*m))
    elif mgh == "h":
        m = int(input("mass\n"))
        g = int(input("gravity\n"))
        pe = int(input("potential energy\n"))
        print(pe/(g*m))    
elif peke == "KE":
    vm = input("ke, m, v\n").lower()
    if vm == "ke":
        v = int(input("velocity\n"))
        m = int(input("mass\n"))
        print(((v ^ 2) * 1/2) * m)
    elif vm == "m":
        ke = int(input("kinetic energy\n"))
        v = int(input("height\n"))
        print(2*ke/(v^2))
    elif vm == "v":
        ke = int(input("kinetic energy\n"))
        m = int(input("mass\n"))
        print(sqrt(2*ke/m))