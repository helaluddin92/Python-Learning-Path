# >>---------------------> Q & A 1 <-------------------------<<

# Write a program that will take a number from the user and determine the average of that number.


number = int(input("Enter a number: "))
count = []
for x in range(0, number):
    element = int(input("Enter element of sum: "))
    count.append(element)

average = sum(count)/number
print("The average of the number is ", average)


# >>---------------------> Q & A 2 <-------------------------<<
# Write a program that will subtract the number from the sum and the result of the two numbers.

def subtract_of_sum(a, b):
    num1 = (a+b)/2
    num2 = (a-b)/2
    print(f"The numbers are {num1} & {num2}")


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
result = subtract_of_sum(x, y)
result


# >>---------------------> Q & A 3 <-------------------------<<
# Write a number from user and will return reverse of the number

num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = (rev*10)+(num % 10)
    num = num//10  # Return Floor division of num

print(rev)

# >>---------------------> Q & A 4 <-------------------------<<

# Write a program that will subtract all the numbers that are divisible by all the numbers in the sleeper.

num = int(input("Enter a number: "))
start = int(input("Starting point: "))
end = int(input("Ending Point"))
for n in range(start, end+1):
    if n % num == 0:
        print(n)
    else:
        print("No number found in the range that divided by {0}".format(num))
        break

# >>---------------------> Q & A 5 <-------------------------<<
# Read Two Numbers and Print Quotient and Remainder


def quotient_and_reminder(num1, num2):
    return f"The quotient of two number is {num1//num2} and reminder is {num1 % num2}"


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = quotient_and_reminder(num1, num2)
print(result)


# >>---------------------> Q & A 6 <-------------------------<<
# Write a number that returns sum of all digit of the number.

num = int(input("Enter a number: "))
sum_num = 0
while num > 0:
    sum_num = sum_num + (num % 10)
    num = num//10

print(sum_num)


# >>---------------------> Q & A 7 <-------------------------<<
# Get a number from input and return prime while it is prime and not prime while it is not prime


number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

# >>---------------> Q & A 7 Another way <------------------<<

number = int(input("Enter a number: "))
if number == 2:
    print("Your given number is prime")
elif number > 2:
    for n in range(3, number):
        if number % n == 0:
            x = number//2
            print("The given number is not prime")
            exit()
    else:
        print("The given number is prime")


# >>---------------------> Q & A 8 <-------------------------<<
# Write a number which will print it's multiplication-table.

number = int(input("Enter a number: "))
for num in range(1, 11):
    print(f"5 X {num} = {num*number}")

