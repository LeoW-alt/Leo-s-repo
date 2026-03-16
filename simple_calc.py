#Calculator Functions

def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("%.2f + %.2f = %.2f"%(num1, num2, result))

def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("%.2f - %.2f = %.2f"%(num1,num2,result))

def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print("%.2f x %.2f = %.2f"%(num1,num2,result)) 

def division():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    while num2 == 0:
        print("Error: Division by zero is not possible")
        num2 = float(input("Enter second number: "))
    
    result = num1/num2
    print("%.4f ÷ %.4f = %.4f"%(num1,num2,result))    

def floor_division():
    int1 = int(input("Enter first integer: "))
    int2 = int(input("Enter second integer: "))
    while int2 == 0:
        print("Error: Division by zero is not possible")
        int2 = int(input("Enter second integer: "))
    quotient = int1 // int2
    remainder = int1 % int2    
    if remainder == 0:
        print("%.0f ÷ %.0f = %.0f"%(int1,int2,quotient))
    else:
        print("%.0f ÷ %.0f = %.0f r %.0f"%(int1,int2,quotient,remainder))

def exponent():
    base = float(input("Enter base: "))
    expo = float(input("Enter exponent: "))
    result = base ** expo
    print("%.2f power %.2f = %.2f"%(base,expo,result))

#Main Program

while True:
    print("\n==== SIMPLE CALCULATOR ====\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Exponentiation")
    print("0. Exit")

    choice = int(input("Choose an operation (0-6): "))

    match choice:

        case 0:
            print("Exiting calculator. Goodbye!")
            break

        case 1:
            add()
        case 2:
            subtraction()
        case 3:
            multiplication()
        case 4:
            division()
        case 5:
            floor_division()
        case 6:
            exponent()
        case _:
            print("Error: Invalid choice. Please select (0-6).")            
