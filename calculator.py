# calculator.py

def add (x, y) :
	z = x + y
	print("{} + {} = {}".format(x,y,z))
	return z

def subtract (x,y) :
	z = x - y
	print("{} - {} = {}".format(x,y,z))
	return z

def multiply (x,y) :
	z = x * y
	print("{} * {} = {}".format(x,y,z))
	return z

def divide (x,y) :
	z = x / y
	print("{} / {} = {}".format(x,y,z))
	return z

x = input("Enter a first number: ")
y = input("Enter a second number: ")
z = input("Enter a operation: ")
a = float(x)
b = float(y)
print("Two numbers are {} and {}. Operation is {}".format(x,y,z))
if z == "add":
	add(a, b)
elif z == "subtract":
	subtract(a,b)
elif z == "multiply":
	multiply(a,b)
elif z == "divide":
	divide(a,b)
else:
	print("The {} operation is not recognized.".format(z))
print("DONE")