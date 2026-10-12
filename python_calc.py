

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

def calculate_percentage(number, total):
    return (number / total) * 100


while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check even/odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", addition(num1, num2))

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", subtraction(num1, num2))

    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", multiplication(num1, num2))

    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", division(num1, num2))

    elif choice == "5":
        number = int(input("Enter an integer: "))
        check_even_odd(number)

    elif choice == "6":
        number = float(input("Enter the number: "))
        total = float(input("Enter the total: "))

        if total == 0:
            print("Error: Total cannot be zero.")
        else:
            percentage = calculate_percentage(number, total)
            print("Percentage:", percentage, "%")

    elif choice == "7":
        print("Exiting calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-7.")
                      

    
          
    

    



