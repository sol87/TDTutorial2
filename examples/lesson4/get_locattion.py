import turtle

def print_location(x, y):
    print x, y
    
    
wn = turtle.Screen()
wn.onclick(print_location)