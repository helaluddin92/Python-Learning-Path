a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

s = ((b**2)-4*a*c)  # s= (b**2 - 4ac)
try:
    if s > 0:
        x1 = (-b+(s)**(0.5))/(2*a)
        x2 = (-b-(s)**(0.5))/(2*a)
        print("There are two real root %0.2f and %0.2f" % (x1, x2))

    elif s == 0:
        x1 = x2 = (-b)/(2*a)
        print("There is only one real root %0.2f and %0.2f" % (x1, x2))
    elif s < 0:
        x1 = (-b+(s)**(0.5))/(2*a)
        x2 = (-b-(s)**(0.5))/(2*a)
        print("There are no real root. There are two complex root %0.2f+%0.2fj" %
              (x1.real, x1.imag) + " and " + "%0.2f%0.2fj" % (x2.real, x2.imag))

except Exception as e:
    print("'a' can't be zero")
