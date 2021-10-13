og = input("What message would you like to decode?\n").upper()
key = input("What is your keyword?\n").upper()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new = ""
for i in range(len(og)):
    if og[i].isalpha():
        change_by = alpha.find(key[i % len(key)]) + 1
        og_val = (alpha.find(og[i]) - change_by + 26) % 26
        new += alpha[og_val]
    else:
        new += og[i]
print(new)