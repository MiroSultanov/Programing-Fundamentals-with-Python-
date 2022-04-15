# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons. 
# The input holds two lines: the number of people N and the capacity P of the elevator.

from math import ceil

number_of_people = int(input())
capacity_of_elevator = int(input())

courses = ceil(number_of_people / capacity_of_elevator)

print(courses)

