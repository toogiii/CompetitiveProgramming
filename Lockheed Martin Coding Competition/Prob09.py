cases = int(input())
f = 0
total = ""
for case in range(cases):
    f += 1
    read = input()
    l = 0
    i = 0
    j = 1
    line = read.split(",")
    for l in range(len(line)):
        line[l] = int(line[l])
        l += 1
    line.sort(reverse = True)
    if f != cases:
        while line[len(line) - 1] != 0:
            if line[i] > line[j]:
                line.append(line[i] - line[j])
                total = total + str(line[i]) + "-" + str(line[j]) + "=" + str(line[len(line) - 1]) + "\n"
            else:
                line.append(line[j] - line[i])
                total = total + str(line[j]) + "-" + str(line[i]) + "=" + str(line[len(line) - 1]) + "\n"                
            i += 1
            j += 1
        if line[len(line) - 2] == 1 and line[len(line) - 3] == 1:
            total = total + "COPRIME\n"
        else:
            total = total + "NOT COPRIME\n"
    else:
        while line[len(line) - 1] != 0:
            if line[i] > line[j]:
                line.append(line[i] - line[j])
                total = total + str(line[i]) + "-" + str(line[j]) + "=" + str(line[len(line) - 1]) + "\n"
            else:
                line.append(line[j] - line[i])
                total = total + str(line[j]) + "-" + str(line[i]) + "=" + str(line[len(line) - 1]) + "\n"                
            i += 1
            j += 1       
        if line[len(line) - 2] == 1 and line[len(line) - 3] == 1:
            total = total + "COPRIME"
        else:
            total = total + "NOT COPRIME"  
print(total)