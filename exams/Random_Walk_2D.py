import numpy as np
import matplotlib.pyplot as plt
import random
def randomwalk2D(n):
    # [0, 0, 0, ... ,0]
    x = np.zeros(n)
    y = np.zeros(n)

    # to hold x and y vals of current loop run
    temp_x = 0 
    temp_y = 0
    L = 0 #to hold number of distinct locations of the current loop run

    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    for i in range(n):
        # Pick a direction at random
        step = random.choice(directions)
        
        # Move the object according to the direction
        if step == "RIGHT":
            temp_x = x[i - 1] + 1
            temp_y = y[i - 1]
        elif step == "LEFT":
            temp_x = x[i - 1] - 1
            temp_y = y[i - 1]
        elif step == "UP":
            temp_x = x[i - 1]
            temp_y = y[i - 1] + 1
        elif step == "DOWN":
            temp_x = x[i - 1]
            temp_y = y[i - 1] - 1

        #checks if the current coordinates are unique so far
        for index, x_val in enumerate(x):
            if temp_x == x_val and temp_y == y[index]: #checks if x value is unique and if, at that x value, the y-coordinates match up too
                break #if yes, not a unique point
        else: #if entire list has been checked without loop breaking, unique point
            L += 1

        #adds the current x& y coordinates to the list of points
        x[i] = temp_x 
        y[i] = temp_y

    # Return all the x and y positions of the object and number of distinct locations
    return x, y, L

x_data, y_data, _ = randomwalk2D(1000)

accum_L = [] #to hold the # of distinct locations (L) from each run
steps = 1000

for i in range(10000): #10,000 sets of walks
    _, _, L = randomwalk2D(steps) #gets just the number of distinct locations
    accum_L.append(L)
    print("running", i)

#finds the mean of the number of distinct locations
mean_L = np.mean(np.array(accum_L))

print(f"mean (10000) of {steps} steps: {mean_L}")

#shows the random walk graph of the first run
plt.title("2D Random Walk in Python")
plt.plot(x_data, y_data)
plt.show()

"""
L(10) = 7
L(100) = 48
L(500) = 196
L(1000) = 363
L(2000) = 673

The rate L per n, the number of distinct locations arrived at per the total number of steps, 
increases at a decreasing rate (but very slightly so that it could (maybe?) effectively be at a constant rate.) 
"""