goal = input("What is your goal at 100%? Please type minutes if it is in minutes.\n")
goal_num = None
minutes = True

if "minute" in goal:
    goal_num = goal.replace(":", ".").split(" ")
    for i in goal_num:
        try:
            goal_num = str(float(goal_num[i]))
        except:
            continue
    goal_num.split(".")
    goal_num = int(goal_num[0]) * 60 + int(goal_num[1])