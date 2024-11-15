# Import the turtle module for creating graphics
import turtle  

# Import the time module for adding delays
import time  

# Create a turtle object to draw on the screen
t = turtle.Turtle()  

# Create a screen object to set the background and other properties
s = turtle.Screen()  

# Define a list of colors to use for the drawing
colors = ['orange', 'red', 'magenta', 'blue', 'green',
          'yellow']  

# Set the background color of the screen to black
s.bgcolor('black')  

# Set the thickness of the turtle's pen
t.pensize('2')  

# Set the speed of the turtle's movement (10 is the fastest setting)
t.speed(10)  

# Loop 240 times to create the pattern
for x in range(240):
    # Change the pen color based on the current loop index
    # x % 6 ensures the index cycles between 0 and 5, picking colors from the list
    t.pencolor(colors[x % 6])  
    
    # Gradually increase the pen's width as x grows larger
    t.width(x // 100 + 1)  
    
    # Move the turtle forward by x units (distance increases with each iteration)
    t.forward(x)  
    
    # Rotate the turtle 59 degrees to the right, creating a spiral effect
    t.right(59)  
    
    # Hide the turtle cursor during drawing for a cleaner look
    turtle.hideturtle()  

# Pause for 3 seconds after the drawing is complete so the user can view it
time.sleep(3)  

# Close the turtle graphics window after the pause
turtle.bye()  
