from time import *
from random import random

# Initialize wait time

wait_time = 3.0

# Check if you lost

lose = 0

# Initialize round number

rounds = 1

# Until you lose

while lose == 0:
    
    # Stores the correct answer
    
    order = []
    for i in range(rounds):
        
        # Picks a random number and prints the corresponding color, then hides it
        
        sleep(wait_time)
        color = round(random() * 3)
        if color == 0:
            print("G")
            order.append("G")
        elif color == 1:
            print("R")
            order.append("R")
        elif color == 0:
            print("Y")
            order.append("Y")
        else:
            print("B")
            order.append("B")
        sleep(wait_time)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
    # Asks for correct answer    
        
    user = input("What was the order? Please use only letters, spaces in between letter, and in uppercase: \n\n")
    
    # Checks if correct
    
    if user.split(" ") == order or user == order[0]:
        print("You got it!")
    else:
        print("You lose. You got to round", str(rounds) + ".")
        lose += 1    
    
    # 20% increase in speed every 3rd level    
        
    if rounds % 3 == 0:
        wait_time = wait_time * .8
        
    # Next round
        
    rounds += 1    
    sleep(3)