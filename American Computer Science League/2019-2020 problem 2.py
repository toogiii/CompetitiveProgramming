def sumOfLastRow(s, d, r):
    # Write your code here
    s_temp = s
    s = 0
    for i in range(len(str(s_temp))):
        s += s_temp % 10 * (8 ** i)
        s_temp = s_temp // 10
    d_temp = d
    d = 0
    for i in range(len(str(d_temp))):
        d += d_temp % 10 * (8 ** i)
        d_temp = d_temp // 10
    f = 0
    triangle = []
    for i in range(1, r + 1): 
        temp = []
        for j in range(0, i):
            n = s + d * f
            temp.append(str(oct(n)))
            f += 1
        triangle.append(temp)  
    # sum digits of last row
    sum_num = 0
    for i in range(len(triangle[r - 1])):
        for j in range(len(triangle[r - 1][i])):
            if triangle[r - 1][i][j] in "0123456789":
                sum_num += int(triangle[r - 1][i][j])
    print(sum_num)
    return sum_num
sumOfLastRow(100000, 100000, 1000000)
