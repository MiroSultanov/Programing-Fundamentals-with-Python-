# Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on the console

def calc_area(width, height):
    return width * height

current_width = int(input())
current_height = int(input())

print(calc_area(current_width, current_height))
