number = int(input("What is your number?")) #asks for input and converts it to integer 
number2 = int(input("What is your second number?")) #asks for second input and converts it to integer


def findgcf(number,number2): #function 
    if number > number2: 
        small = number2
    else: 
        small = number 
    for i in range (1, number+1):
        if (number%i == 0) and (number2%i == 0):
            gcf = i

    return(gcf)

print(f"This is the GCF {findgcf(number,number2)}")
            




