import math #imports the math library

number = float(input("What is your number?")) #asks for input and converts it to decimal
number2 = float(input("What is your second number?")) #asks for second input and converts it to decimal
num = int(number) #converts first input to integer
num2 = int(number2) #converts second input to integer

x = math.gcd(num,num2) #finds the greatest common denominators/factors of first input and second input
print (f"This is the greatest common factor: {x}") #prints message & the greatest common factor


 


