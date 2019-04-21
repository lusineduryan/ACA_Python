# Type the name, age and height, so that the height number is 2 digits precised.

name = input()
age = int(input())
height = float(input())

height_format = '{:04.2f}'.format(height)
print(f"Hi, my name is {name}. My age is {age} and my height is {height_format}.")

print("Hi, my name is %s. My age is %d and my height is %.2f." % (name, age, height))