num1 = int(input("Give the value of 1: "))
num2 = int(input("Give the value of 2: "))
operator = input("Give operator: ")

if operator == "+":
    print(f"Addition of two number {num1+num2}")
elif operator == "-":
    print(f"Subtraction of two number {num1-num2}")
elif operator =="*":
    print(f"Multiplication of two number {num1*num2}")
elif operator == "/":
    print(f"Division of two number {num1/num2}")
else:
    print("invalid operator")
