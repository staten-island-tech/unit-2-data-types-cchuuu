#Data type
#1  and "1" are not the same
def add(x, y):
    print(x + y)
add(1,2)

name = "Chu"
def greeting(person):
    print(person)
greeting(name)

#undefined/null
#booleans = true/false

tenure = True
def is_tenured (status):
    if(status == True):
        print("They have tenure")
    else: 
        print("They are not tenured")

is_tenured(tenure)