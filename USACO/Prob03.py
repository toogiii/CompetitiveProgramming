num = int(input())
total = []
guesses = [0,0,0]
swaps = []
pos = ["1", "2", "3"]
storage = ""
for i in range(0, num):
    data = input().split(" ")
    swaps.append(data[0])
    swaps.append(data[1])
    guesses.append(int(data[2]))
for i in range(0, num):
    if pos.index(swaps[i * 2]) < pos.index(swaps[i * 2 + 1]):
        storage = pos[pos.index(swaps[i * 2 + 1])]
        pos[pos.index(swaps[i * 2 + 1])] = pos[pos.index(swaps[i * 2])]
        pos[pos.index(swaps[i * 2])] = storage
    else:
        storage = pos[pos.index(swaps[i * 2])]
        pos[pos.index(swaps[i * 2])] = pos[pos.index(swaps[i * 2 + 1])]
        pos[pos.index(swaps[i * 2 + 1])] = storage
    print(pos)
    if pos[0] == '1':
        guesses[0] += 1
    elif pos[1] == '1':
        guesses[1] += 1
    else:
        guesses[2] += 1
loc = max(guesses)
print(loc)