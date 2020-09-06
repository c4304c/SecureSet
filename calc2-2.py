

#!/usr/bin/python3
#says program name
print("Basic Calculator 2")

# Defines Functions
def addition(x, y):
    answer = x + y
    return answer

def subtraction(x, y):
    answer = x - y
    return answer

def multiplication(x, y):
    answer = x * y
    return answer

def division(x, y):
    answer = x / y
    return answer
    #user chooses 2 numbers
def main():
    x = int(input("Pick your first number?  "))
    y = int(input("Pick your second number?  "))

#behind the scene math work and output answer and choice of math chosen
    choice = input("Please choose 'add', 'sub', 'mul', or 'div'?   ")
    if choice == "add":
        answer = addition(x, y)
        print(answer)
    elif choice == "sub":
        answer = subtraction(x, y)
        print(answer)
    elif choice == "mul":
        answer = multiplication(x, y)
        print(answer)
    elif choice == "div":
        answer = division(x, y)
        print(answer)
#user must choose 'add', 'sub', 'mul', or 'div
    else:
        print("Please only type 'add', 'sub', 'mul', or 'div'")

# Pulls function to use User's numbers
main()


