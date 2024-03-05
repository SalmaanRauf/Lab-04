# main.py
from mathematics import *
from mathematics.numbers.series import calculate_sum, average
from mathematics.numbers.simple import *
from mathematics.geometry import *

# Test the functions
print(getname())



numbers_values = {'a': 1, 'b': 2, 'c': 3}
print(calculate_sum(**numbers_values))
print(average(**numbers_values))

print(addition(left=5, right=3))
print(subtraction(left=5, right=3))
print(multiplication(left=5, right=3))
print(division(left=5, right=3))

print(circumference(radius=2))
print(circle_area(radius=2))

print(surface_area(side=3))
print(volume(side=3))
