#Calculator function using lambda, map, reduce, filter and generator
#student number: 10370112, Benish, CA no:4
import math
##########################################addition
add = lambda x, y : x + y
print add(5,5)
##############
x = [1,2,3]
y = [4,5,6]
from operator import add
print map(add, x, y)
###############
##########################################subtraction
sub = lambda x, y : x - y
print sub(100,5)
##########################################multiplication
multi = lambda x, y : x * y
print multi(15,5)
#############
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print product
###################
n=[4,3,2,1]
print (reduce(lambda x,y:x*y,n))
#############################################division
div = lambda x, y : x / y
print div(25,5)
###############################################square
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print squared
########
def square(values):
	return map(lambda x: x*x, values)
print square([47, 11, 42, 13])
###################
squares = map(lambda x: x**2, range(10))
print squares
####################using generator
def square_numbers(nums):
	for i in nums:
		yield(i*i)
my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
	print num
########################################################squareroot
def square_root(values):
	return map(lambda x: math.sqrt(x), values)
print square_root([2209,121,1764,169])
####################################################cube
def cube(x):
    return (x**3)
funcs = [cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value
######################################################## sin function
def sinradian(numbers):
	return map(lambda x:math.sin(x),numbers)
print sinradian([90,30,60])
#################
def sindegree(numbers):
	return map(lambda x:math.sin(math.radians(x)),numbers)
print sindegree([90,30,0])
#####################################################cos function
def cosradian(numbers):
	return map(lambda x:math.cos(x),numbers)
print cosradian([90,30,60])
#################
def cosdegree(numbers):
	return map(lambda x:math.cos(math.radians(x)),numbers)
print cosdegree([90,30,0])
########################################### tan function
def tanradian(numbers):
	return map(lambda x:math.tan(x),numbers)
print tanradian([90,30,60])
#################
def tandegree(numbers):
	return map(lambda x:math.tan(math.radians(x)),numbers)
print tandegree([90,30,0])



