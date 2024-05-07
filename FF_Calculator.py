import re

print("Welcome to calcultor")
print("type quit to quit")
previous = 0
run = True

def math():
    global run, previous
    if previous == 0:
        equation = input("enter your number ")
    else:
        equation = input("enter new number")
    if equation == '0':
        run = False
    else:
        equation = re.sub('[a-z,A-Z.]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("your number", previous)


while run:
    math()


