# Find even and odd number

for num in range(0, 101):
    if num % 2 == 0:  # Even Number because every even number divided by 2 without remains
        print("Even Number")
    else:  # Odd number can't divided by 2 without remains
        print("Odd Number")

# Sum of all even number
# Sum of all odd number

number = 100
total_even = 0
total_odd = 0
n = 1

for num in range(number):
    if num % 2 == 0:
        total_even += n
    else:
        total_odd += n
    n += 1

print(total_even)
print(total_odd)


# Sum of square of all odd and even number till 1 to 100

# ===========================Odd Number============================


def sum_odd_square(nums):
    total = 0
    for number in range(0, nums+1):
        if number % 2 != 0:  # Odd Number
            total += (number**2)
    return total


result = sum_odd_square(100)
print(result)
# ============================Even Number==========================


def sum_even_square(nums):
    total = 0
    for number in range(0, nums+1):
        if number % 2 == 0:  # Even Number
            total += (number**2)
    return total


result = sum_even_square(100)
print(result)
