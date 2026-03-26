def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return"Division by zero is not allowed."
    return a/b

while True:
    print("Select operation: +, -, *, /")
    choice=input("Enter choice: ")

    while choice not in ['+','-','*','/']:
        print("Invalid choice. Please select a valid operation.")
        choice=input("Enter choice: ")

    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    if choice=="+":
        print("Result:", (add(num1,num2)))
    elif choice=="-":
        print("Result:", (subtract(num1,num2)))
    elif choice=="*":
        print("Result:", (multiply(num1,num2)))
    elif choice=="/":
        print("Result:", (divide(num1,num2)))
    else:
        print("Invalid input")

    again = input("Do you want to perform another operation? (y/n): ")
    if again.lower() != 'y':
        break
