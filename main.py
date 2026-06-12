a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("Enter an operator (+, -, *, /): ")

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