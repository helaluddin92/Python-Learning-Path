# Calculate how many prime number between 1 and 100


def prime_number(num):
    primes = [2]  # Initial value setup. Lower prime number is 2
    x = 3  # Initial value for total prime number
    if x < 2:  # Lower prime number is 2
        return 0
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return primes


result = prime_number(100)
print(result)
print("Total Prime Number From 1 to 100 is", len(result))
