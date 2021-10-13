cases = int(input())
j = 0
total = ""
for case in range(cases):
    read = input()
    c = -1
    i = 0
    j += 1
    nums = read.split(",")
    nums[0] = int(nums[0])
    nums[1] = int(nums[1])
    a = max(nums)
    b = min(nums)
    while c != 0:
        c = a - b
        total = total + str(a) + "-" + str(b) + "=" + str(c) + "\n"
        a = max(b,c)
        b = min(b,c)
    if j != cases:
        if a == 1:
            total = total + "COPRIME\n"
        else:
            total = total + "NOT COPRIME\n"
    else:
        if a == 1:
            total = total + "COPRIME"
        else:
            total = total + "NOT COPRIME"        
print(total)