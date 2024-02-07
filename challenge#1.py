x = "Bill"
y = "Tip"
z = "TotalAmount"
total = 0
tip = 0
message = "Here's your total."


x = float(input("How much was your meal?"))

y = input("How was our service?")
if y == ("Bad"):
    print("0% Tip")
    tip = x * 0
elif y == ("Okay"):
    print("15% Tip")
    tip = x * 0.15
elif y == ("Good"):
    print("20% Tip")
    tip = x * 0.2
elif y == ("Great"):
    print("25% Tip")
    tip = x *0.25

print (tip)
total = x + tip
print (message)
print (total)


