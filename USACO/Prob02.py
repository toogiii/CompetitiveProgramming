cases = int(input())
pairs = []
numbuck = []
for i in range(0, cases):
    data = input().split(" ")
    pairs.append(int(data[0]))
    pairs.append(int(data[1]))
    numbuck.append(int(data[2]))
using = []
for j in range(0, max(pairs)):
    per = 0
    for a in range(0, int(len(pairs) / 2)):
        if pairs[a * 2] - j <= 0 and pairs[a * 2 + 1] - j >= 0:
            per = per + numbuck[a]
    using.append(per)
print(max(using))