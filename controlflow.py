# result = int(input("Enter result: "))

# if 80 <= result <= 100:
#     print("A")

# elif 60 <= result <= 79:
#     print("B")

# elif 40 <= result <= 59:
#     print("C")

# else:
#     print("Fail")


a = 12
b = 13
c = 15

if a > b:
    if a > c:
        print(f"{a} is big number")
    else:
        print(f"{c} is big number")
elif b > c:
    if b > c:
        print(f"{b} is big number")
    else:
        print(f"{c} is big number")
else:
    if c > b:
        print(f"{c} is big number")
    else:
        print(f"{b} is big number")
