while True:
    try:
        num1 = float(input("enter first number: "))
        operation = input("enter operation (+, -, *, /): ")
        num2 = float(input("enter second number: "))
    except ValueError:
        print("please enter a valid number")
        continue

    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 == 0:
            print("can't divide by zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("the operation is not valid")

    again = input("do you want to continue (yes/no): ")
    if again == "no":
        print("thank you for using the calculator")
        break
