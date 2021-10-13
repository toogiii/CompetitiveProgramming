import math
numbers = [int(i) for i in input("Enter two whole numbers: ").split(" ")]
print("GCD: " + str(math.gcd(numbers[0], numbers[1])))