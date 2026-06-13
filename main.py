c = input("Enter an operator (+, -, *, /): ")

if c == "^":
    a = int(input("Enter a number: "))
    def square(a):
        return a ** 2
    result = print(square(a))

elif c == "sqrt":
    a = int(input("Enter a number: "))
    def square_root(a):
        return a ** 0.5
    result = print(square_root(a))
    
elif c == "cube":
    a = int(input("Enter a number: "))
    def cube(a):
        return a ** 3
    result = print(cube(a))

else:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if c == "+":
        result = a + b

    elif c == "-":
        result = a - b

    elif c == "*":
        result = a * b

    elif c == "/":
        if b != 0:
            result = a / b

    elif c == "%":
        if b != 0:
            result = (a * b)/100

        else:
            result = "Error: Invalid operator."

    print("Result:", int(result))