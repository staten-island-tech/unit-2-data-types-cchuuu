number = int(input("What is your number?")) #asks for input and converts it to integer 
number2 = int(input("What is your second number?")) #asks for second input and converts it to integer


def findgcf(number,number2): #function 
    if number > number2: 
        small = number2
    else: 
        small = number 
    for i in range (1, number+1): #i in range of 1 and (first input + 1)
        if (number%i == 0) and (number2%i == 0): #if the remainder of first input and second input is 0
            gcf = i #

    return(gcf) #returns the value to the function

print(f"This is the GCF, {findgcf(number,number2)}") #prints out the GCF
            




