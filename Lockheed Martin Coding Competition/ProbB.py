import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    case = sys.stdin.readline().rstrip().split(":")
    speed = float(case[0])
    distance = float(case[1])
    if speed == 0:
        print("SAFE")
    elif distance / speed <= 1:
        print("SWERVE")
    elif distance / speed <= 5:
        print("BRAKE")
    else:
        print("SAFE")