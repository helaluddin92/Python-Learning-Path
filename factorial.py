# >>---------------------> Q & A <-------------------------<<
# Find factorial of any given number

# --------------------First Way-------------------------------
num = int(input("Enter a number: "))
total = 1
for i in range(num, 0, -1):  # n! = n*(n-1)*(n-2)*....2*1
    total *= i

print(total)


# -------------------Second Way--------------------------------
num = int(input("Enter a number: "))
total = 1
i = 1
while(i <= num):
    total *= i
    i += 1
print(total)

# --------------------Third Way----------------------------------


def factorial(n):
    if n == 1:
        result = 1
    elif n == 0:  # 0! = 1
        result = 1
    else:
        result = n * factorial(n-1)
    return result


print(factorial(5))
