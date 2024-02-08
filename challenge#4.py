number = float(input("What is your number?"))
num = int(number)
factors = []

for i in range(1,int(num/2)):
    if num%i == 0:
        if i not in factors:
            factors.append(i)
        if number/i not in factors:
            factors.append(int(num/i))

for i in factors:
    print(i)