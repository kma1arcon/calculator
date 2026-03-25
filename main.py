def add(a,b):
 return a+b

def subtract(a,b):
 return a-b

def multiply(a,b):
 return a*b

def divide(a,b):
 if b==0:
  return"Error: Cannot divide by zero"
 return a/b


print("Select operation: +, -, *, /")
choice=input("Enter choice: ")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

if choice=="+":
 print(add(num1,num2))
elif choice=="-":
 print(subtract(num1,num2))
elif choice=="*":
 print(multiply(num1,num2))
elif choice=="/":
 print(divide(num1,num2))
else:
 print("Invalid input")