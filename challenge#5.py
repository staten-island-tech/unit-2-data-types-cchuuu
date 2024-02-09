number = float(input("What is your number?"))
number2 = float(input("What is your second number?"))
num = int(number)
num2 = int(number2)
factors = []

for i in range(1,int(num2/2)):
    if num%i == 0 and num2%i == 0:
        if i not in factors:
            factors.append(i)
        if number/i and number2/i not in factors:
            factors.append(int(num/i and num2/i))

for i in factors:

    print (i)
 


