import time

def main():
Running = True
while running:
def title():

	print("Welcome to our new and improved calculator!")
	time.sleep(1)
	
	print("This calculator does many things such as:")
	time.sleep(1)
	
	print("1. Missing triangle side (A or B)”)
	time.sleep(0.5)
	
	print("2. Calculate the missing hypotenuse (C).")
	time.sleep(0.5)
	
	print("3. Area of a Circle")
	time.sleep(0.5)
	
	print(“4. Area of a rectangle”)
	time.sleep(0.5)
	
	print(“5. Area of a triangle”)
	time.sleep(0.5)
	
	print(“6. Volume of a cylinder”)
	time.sleep(0.5)
	
	print(“7. Circumference of a circle”)
	time.sleep(0.5)
	
	print(“8. GST + PST”)
	time.sleep(0.5)
	
	print(“9.Addition”)
	time.sleep(0.5)
	
	print(“10.Subtraction”)
	time.sleep(0.5)
	
	print(“11.Multiplication”)
	time.sleep(0.5)
	
	print(“12.Division”)
	time.sleep(0.5)
	
	print(“13.Credits”)
	time.sleep(0.5)
	
	print(“14.Quit”)


Choice = input(“Enter the corresponding number to the formula you would like to choose:”)
try:
If Choice == '1'
	missing_side()
elif choice == '2'
	missing_hypotenuse()
elif choice == '3'
	a_circle()
elif choice == '4'
	a_rectangle()
elif choice == '5'
	a_triangle()
elif choice == '6'
	v_cylinder()
elif choice == '7'
	circumference_circle()
elif choice == '8'
	gst_pst()
elif choice == '9'
	addition()
elif choice == '10'
	subtraction()
elif choice == '11'
	multiplication()
elif choice == '12'
	division()
elif choice == '13'
	credits()
elif choice == '14'
	print(“Bye”)
		running = False
else:
print(“please pick a valid number.”)
except ValueError:
	print(“Invalid Input! Pick a number.”)


def missing_side():
	try:
		A = float(input(“please enter the hypotenuse length.”))
		B = float(input(“please provide the remaining side length you have”))
		C = (A**2 - B**2) ** 0.5
		print(f”the missing value for missing side of {C}.”)
except ValueError
	

def missing_hypotenuse():
	try:
	a = float(input(“Please enter side 1:”))
	b = float(input(“Please enter side 2:”))
	c2 = a ** 2 + b ** 2
	C = c2 ** 0.5

	print(f”{c}”)
except ValueError:
	print(“please enter a valid number.”)

def a_circle():
	try:
		r = float(input(“Enter value for the radius”))
		a = 3.14 * (r**2)
		print(f”{a}”)
	except ValueError:
		print(“please enter a valid number.”)
	
def a_rectangle():
	try:
		L = float(input(“Please enter the length:”))
		W = float(input(“Please enter the width:”))
		A = W * L
		print(f”The area is {A}!”)
	except ValueError:
		print(“please enter a valid number.”)
	

def a_triangle():
	try:
		b = float(input(“Enter value for the base:”))
		h = float(input(“Enter value for the height:”))
		a = (h * b) / 2
		print(f”a”)
	except ValueError:
		print(“please enter a valid number.”)


def v_cylinder():
	try:
		R = float(input(“Please enter the value for the radius.”)
		H = float(input(“Please enter the value for the height.”)
		V = 3.14 * (R**2) * H
		print(f”The volume for the cylinder is {V}.”)
	except ValueError:
		print(“please enter a valid number.”)

def circumference_circle():
	try:
		R = float(input(“please enter the value of the radius:”))
		C = 2 * 3.14 * R
		print(f”The value of the circumference is {R}.”)
	except ValueError:
		print(“please enter a valid number.”)

def gst_pst():
	try:
		C = float(input(“Please enter the value:”))
		T = C * 0.12
		print(f”There will be {T}$ in GST and PST”)
except ValueError:
		print(“please enter a valid number.”)


		
def addition():
	try:
		A = float(input(“Enter first number”))
		B = float(input(“Enter a second number”))
		C = A + B
		print(f”The sum is {C}”)
	except ValueError:
		print(“please enter a valid number.”)
		
def subtraction():
	try:
		A = float(input(“Please enter the first value:”))
		B = float(input(“Please enter the second value:”))
		C = A - B
		print(f”The difference is {C}”.)
	except ValueError:
		print(“please enter a valid number.”)

		

		
def multiplication():
	try:
		A = float(input(“Please enter the first value:”))
		B = float(input(“Please enter the second value:”))
		C = A*B
		print(f”the product is {C}”)

except ValueError:
		print(“please enter a valid number.”)

def division():
try:
	A = float(input(“Please enter the first value:”))
		B = float(input(“Please enter the second value:”))
		C = A / B
		print(f”The quotient is {C}”.)
	except ValueError:
		print(“please enter a valid number.”)
		

def credits():
	print(“Title”


if __name__ == "__main__":
	main()
