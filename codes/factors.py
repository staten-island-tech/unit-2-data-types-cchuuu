number = float(input("What is your number?")) #asks for input and converts it to a decimal
num = int(number) #converts the input to a integer
factors = [] #the factors will go into the brackets

for i in range(1,int(num/2)): #i = factors, in range of 1 and the input divided by 2
    if num%i == 0: #if the remainder of input/i (one of the numbers in the range) = 0, moves onto next code
        if i not in factors: #if i is not in factors
            factors.append(i) #add i into factors
        if number/i not in factors: #if input/i is not in factors
            factors.append(int(num/i)) #add i (converted to integer) into factors

for i in factors: #for values in factors
    print(i) #print the factors