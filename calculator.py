def calculator(number1, condition, number2):
    if condition == '+' or condition == '-' or condition == '*' or condition == '/':
        if condition == '+':
            return number1 + number2
        elif condition == '-':
            return number1 - number2
        elif condition == '*':
            return number1 * number2
        elif condition == '/':
            return number1 / number2
    else:
        return "Please enter + or - or * or / as a condition for add or subtract or multiply or division."


while True:
    n1 = int(input("Enter first number: "))
    c = input("Enter condition eg: +,-,*,/: ")
    n2 = int(input("Enter second number: "))
    result = calculator(n1, c, n2)
    print(result)
