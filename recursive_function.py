# >>---------------------> Q & A 1 <-------------------------<<
# Find factorial of any given number...


def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))  # // Here factorial(n-1) = (n-1)!


n = float(input("Enter a number: "))
print(factorial(n))

# >>---------------------> Q & A 2 <-------------------------<<
#


def try_recursion(k):
    if k > 0:
        result = k + try_recursion(k-1)
    else:
        result = 0
    return result


print(try_recursion(6))


# >>---------------------> Q & A 3 <-------------------------<<
# Get a number from input and return prime while it is prime and not prime while it is not prime

def is_prime(n, i=2):
    if (n <= 2):
        return True if n == 2 else False
    if (n % i == 0):
        return False
    if (i*i > n):
        return True
    return is_prime(n, i+1)


n = 15
if is_prime(n):
    print("This is a prime number")
else:
    print("This is not a prime number")
