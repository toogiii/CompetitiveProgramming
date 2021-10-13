read = open("mixmilk.in", "r")
# Mixing Milk
buckets = []
for line in read:
    buckets.append(line.replace("\n", ""))
# Bucket Data
b1 = buckets[0]
b2 = buckets[1]
b3 = buckets[2]
# Bucket capacity
c1 = int(b1[0:b1.find(" ")])
c2 = int(b2[0:b2.find(" ")])
c3 = int(b3[0:b3.find(" ")])
# Initial fill
m1 = int(b1[b1.find(" "):len(b1)])
m2 = int(b2[b2.find(" "):len(b2)])
m3 = int(b3[b3.find(" "):len(b3)])
i1 = int(b1[b1.find(" "):len(b1)])
i2 = int(b2[b2.find(" "):len(b2)])
i3 = int(b3[b3.find(" "):len(b3)])
# Pour!
for j in range(1,101):
    if j % 3 == 1:
        if m1 + m2 > c2:
            m2 = c2
            m1 = m1 - (c2 - i2)
            i2 = m2
            i1 = m1
        else:
            m2 = m1 + m2
            m1 = 0
            i2 = m2
            i1 = m1
    elif j % 3 == 2:
        if m2 + m3 > c3:
            m3 = c3
            m2 = m2 - (c3 - i3)
            i3 = m3
            i2 = m2
        else:
            m3 = m3 + m2
            m2 = 0
            i3 = m3
            i2 = m2
    else:
        if m3 + m1 > c1:
            m1 = c1
            m3 = m3 - (c1 - i1)
            i1 = m1
            i3 = m3
        else:
            m1 = m1 + m3
            m3 = 0
            i1 = m1
            i3 = m3
# file = open("mixmilk.out", "w")
print(str(m1) + "\n" + str(m2) + "\n" + str(m3), end = "")