# 'https://rszalski.github.io/magicmethods/#representations'

# __new__ Method


class Inch(float):
    # Convert from inch to meter
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg*0.0254)


result = Inch(12)
# print(result)

# __init__ method


class Inch:
    # Convert from inch to meter
    def __init__(self, arg=0.0):
        self.arg = arg * 0.0254


result = Inch(12)
# print(result.arg)


class SomeClass:
    def __init__(self, num="", string=""):
        self.num = 10
        self.string = "Md. Helal Uddin"


result = SomeClass()
# print(result.num)
# print(result.string)


class SomeClass:
    def __init__(self, num, string):
        self.num = num
        self.string = string
        # print(self.num)
        # print(self.string)


SomeClass(20, "Md. Helal Uddin")

# __add__, __sub__, __mul__, __div__, __floordiv__ Method


class AddSomething:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f"{self.x + other.x}, {self.y + other.y}"

    def __sub__(self, other):
        return f"{self.x - other.x}, {self.y - other.y}"

    def __mul__(self, other):
        return f"{self.x * other.x}, {self.y * other.y}"

    def __div__(self, other):
        return f"{self.x / other.x}, {self.y / other.y}"

    def __floordiv__(self, other):
        return f"{self.x // other.x}, {self.y // other.y}"

    def __pow__(self, other):
        return f"{self.x ** other.x}, {self.y ** other.y}"


result = AddSomething(7, 10)
other = AddSomething(10, 20)
x = (result ** other)
# print(x)


class String:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"{self.string}"

    def __str__(self):
        return f"{self.string}"


if __name__ == "__main__":
    string1 = String("Hello")
    # print(str(string1))

# __cmp__, __gt__, __lt__, __eq__, __ne__, ... Method


class Comparison:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __cmp__(self, other):
    #     return (self.x > other.x, self.y < other.y)

    def __gt__(self, other):
        return (self.x > other.x, self.y > other.y)


result = Comparison(50, 60)
other = Comparison(20, 30)
# print(result > other)


# Controlling Attribute Access __getattr__, __setattr__, __delattr__


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
print(cloud.tags)
