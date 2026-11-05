while True :
    num1 = float(input("enter first number"))
    p = input(" enter operation (+ , - , * , / )")
    num2 = float(input("enter second number"))

    if p == "+":
        print(f"{num1 } + { num2 } = {num1 + num2}")
    elif p == "-":
        print(f"{num1 } - { num2 } = {num1 - num2}")
    elif p == "*":
        print(f"{num1 } * { num2 } = {num1 * num2}")
    elif p == "/":
        print(f"{num1 } / { num2 } = {num1 / num2}") 
    else: 
        print("the operation is not valid")

    again = input("do you want to continue (yes/no) : ")
    if again == "no":
            print("thank you for using the calculator")
            break
