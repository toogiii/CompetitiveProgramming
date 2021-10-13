num_animals = int(input())
data = []
chars = []
animals = []
sims = []
for i in range(0, num_animals):
    data.append(input().split(" "))
for i in range(0, len(data)):
    chars.append(data[i][1:])
    animals.append(data[i][0])
for i in range(0, len(chars)):
    f = 0
    for j in range(0, int(chars[i][0])):
        if sum([k.count(chars[i][j + 1]) for k in chars]) > 1:
            f += 1
    sims.append(f)
print(max(sims) + 1)