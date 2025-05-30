import matplotlib.pyplot as plt
import math

base_initial_v = 10 #m/s. initial velocity
base_angle = 10 #degrees above horizontal
base_initial_h = 10 #m. initial height above 0/ground
vert_accel = -9.81 #m/s^2. vertical acceleration/gravity
colors = ['red', 'orange', 'yellow'] #colors of arc

for i in range(3): #one loop for each arc
    
    #to hold the x and y values of the individual arc
    x_values = [] 
    y_values = []

    #alters the base values/variables for each arc
    initial_v = base_initial_v + 2*i
    angle = math.radians(base_angle + 20*i)
    initial_h = base_initial_h + 5*i
    
    #calculates the x and y components of the initial velocity. 
    v_x = math.cos(angle) * initial_v #isn't "intiial" because it remains constant
    #print(i, v_x)
    initial_v_y = math.sin(angle) * initial_v
    #print(i, initial_v_y)

    #finds the time when y=0/the object hits the ground
    #end_time = (2*(initial_h))/(math.sqrt(initial_v_y**2 - 2*vert_accel*initial_h)+initial_v_y) ... doesn't work
    end_time = ((-initial_v_y - math.sqrt(initial_v_y**2 - 4*(.5*vert_accel)*(initial_h)))/vert_accel)
    #print("time", end_time)
    
    #for every sec/50, plots the objects x and y coordinates
    for t in range(0, int(end_time * 50)):
        time = t * .02

        x = v_x * time
        y = (initial_v_y * time) + 0.5*vert_accel*(time**2) + initial_h
        x_values.append(x)
        y_values.append(y)

    plt.scatter(x_values, y_values, label= f"Arc {i+1}", color= colors[i]) #plots the points

#graph creation
plt.xlabel("horizontal distance (meters)")
plt.ylabel("vertical distance (meters)")
plt.legend()
plt.show()
