def intBase(number, base):
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        digits.append(number % base)
        number = number // base
    return digits[::-1]

digitList = "123456789ABC"
base13Num = ""

number = int(input("Enter your decimal whole number: "))
numDigits = intBase(abs(number), 13)

for item in numDigits:
    base13Num += digitList[item - 1]
if number < 0:
    print("-" + str(base13Num))
else:
    print(base13Num)