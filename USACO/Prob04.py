num_cows = input()
order = input().split(" ")
for i in range(0, len(order)):
    order[i] = int(order[i])
finished = []
for a in range(0, max(order)):
    finished.append(a + 1)
print(finished)
f = 0
while finished != order:
    if order[0] == max(order):
        order.insert(len(order)-1, order.pop(0))
    elif order[0] == min(order):
        order.insert(order.index(max(order)), order.pop(0))
    else:
        order.insert(order.index(order[0] - 1), order.pop(0))
    print(order)
    f += 1
print(f)