number = int(input("What is your number?")) #asks for input and converts it to integer 
number2 = int(input("What is your second number?")) #asks for second input and converts it to integer
factors = []

for i in range (1, number+1): #i in range of 1 and (first input + 1)
    if (number%i == 0) and (number2%i == 0): #if the remainder of first input and second input is 0
        factors.append(i) #add i into factors

print(f"This is the GCF, {factors[-1]}") #prints out the GCF
            




