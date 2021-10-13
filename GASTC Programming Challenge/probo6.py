first_line = True
for line in open("Prob05.in.txt", "r")
    line_text = line.strip("\n")
    if line_text > 69:
        print("PASS")
    else:
        print("FAIL")