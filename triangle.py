# Check whether triangle is valid or not if sides are given

print("Enter three side of a triangle")


def triangle(x, y, z):
    if ((x+y > z) and (x+z > y) and (y+z > x)):
        return "This is a valid triangle"
    else:
        return "This is not a valid triangle"


a = int(input("Enter first length: "))
b = int(input("Enter second length: "))
c = int(input("Enter third length: "))

result = triangle(a, b, c)
print(result)


# Area of a triangle
# A = \sqrt{s(s-a)(s-b)(s-c)},

a = 5
b = 6
c = 7

# a = int(input("Enter the first side of triangle: "))
# b = int(input("Enter the second side of triangle: "))
# c = int(input("Enter the third side of triangle: "))

s = (a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** .5
print("The area of the triangle is %.3f" % area)
