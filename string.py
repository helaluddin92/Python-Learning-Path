# =============Python String===============

print("Hello World")
name = "Md. Helal Uddin"
print(name)

# ============Assign String=================
# 1. Single line string
# 2. Multi line string

string = "I am learning python"
string1 = """The quick brown fox, jumps over the lazy dog"""
string2 = 'I am going to school'


# ================String Slicing============

print(string[0])  # First character
print(string[0:])  # Start to end
print(string[:-1])  # start to second last
print(string[-6:])  # last to last sixth character
print(string[0::1])  # Start to end and step 1
print(string[0:10:2])  # Start to tenth character and step 2
print(string[::-1])  # Reverse


# ============= String Length ===============

print(len(string))  # Shows total character of string.
print(len(string1))
print(len(string2))

# ============== String Concatanation==============

string3 = "The quick brown fox"
string4 = "Jumps over the lazy dog"

print(string3 + ', ' + string4 + '.')


# =============== Check String ======================

find_letter_the = 'T' in string3
# Boolean type, return True because "T" in "string3"
print(find_letter_the, type(find_letter_the))

find_word_hello = "hello" in string3
# Return false "hello" is not in "string3"
print(find_word_hello, type(find_word_hello))


# ============== String Formatting =====================

x = 20
y = 30
print(f'The sum of two value is {x + y}')
z = x + y
print("The sum of two value is {}".format(z))

price = 300
quantity = 10
itemno = 3250
myorder = "I want to pay {0} dollars for {1} piece of item {2}"
print(myorder.format(price, quantity, itemno))

point = {'x': 4, 'y': -5}
print('{x} {y}'.format_map(point))  # For dictionary type formatting

# ======================Escape Character==================

mystirng = "Hello my name's Helal Uddin"
mystring = 'Hello my name\'s Helal Uddin'  # For single quote
print(mystring)
mystring = "This will insert one backslash\\"  # To get one backslash in line
print(mystring)
# Here get a line break and start new line.
mystring = "Hello my name\'s Helal Uddin \nI am learning Python."
print(mystring)
mystring = "Hello\r World!"  # Carriage return
print(mystring)
mystring = "Hello\tWorld!"  # Get a tab
print(mystring)
mystring = "Hello \bWorld "
print(mystring)  # Get a back space


# ================== String Method ===============================

txt = 'hello and welcome to my world. my name is Helal Uddin'
print(txt.capitalize())  # convert the first character to uppercase
txt = "Hello and WelCome To My World"
print(txt.casefold())  # Convert string into lowercase
print(txt.lower())  # Convert string into lowercase
print(txt.upper())  # Convert string into uppercase
print(txt.title())  # Make uppercase first character of every word
print(txt.replace("hello", "Hello"))  # Replace character which is indicate

# Returns a centered string

txt = "Hello"
print(txt.center(20))
print(txt.center(12, '='))
print(txt.center(50, '-'))

# Returns a right and left justified version of the string
txt = "Hello"
print(txt.rjust(20))  # Right Justify
print(txt.ljust(20))  # Left Justify


# Returns the number of times a specified value occurs in a string

txt = "Hello World! Hello World! Hello World!"
print(txt.count('World!'))
print(txt.count("Hello", 0, 10))  # Value, Start, End

# Returns true if the string ends with the specified value

txt = "Hello World"
print(txt.endswith('d'))  # True
print(txt.endswith('!'))  # False

# Returns true if the string starts with the specified value

txt = "Hello World"
print(txt.startswith('H'))  # True
print(txt.startswith('!'))  # False

# Searches the string for a specified value and returns the position of where it was found

txt = "Hello World"
print(txt.find('o'))
# -1 Means false. Not found in 0 to 5. value, starts, ends
print(txt.find('r', 0, 5))

# Searches the string for a specified value and returns the position of where it was found

# Index method almost same as find method but different is find() returns -1 if not found and index gives if not found.
txt = 'Hello, welcome to my world'
print(txt.index('welcome'))  # 'welcome' starts with index no 7
print(txt.index('e', 4, 12))
# =================================================================

txt = 'mynum12'
print(txt.isalnum())  # Returns True all characters are alphanumeric
txt = "12 my num"
# Return False because here are two space that are not alphanumeric
print(txt.isalnum())

# =================================================================

txt = 'mynumber'
print(txt.isalpha())  # Returns True all characters are alphabet
txt = "12mynum"
print(txt.isalpha())  # Returns False all characters are not alphabet

# =================================================================

number = '12.55'
print(number.isdecimal())  # Returns False "12.55" is not decimal
number = '\u0033'
print(number.isdecimal())  # Returns True this is unicode for 3

# =================================================================
number = '12.55'
print(number.isdigit())  # Returns True

# ================================================================

# ==================Strip Method================================

mystring = "     Hello World    "
print(mystring.strip())  # Remove all whitespace before and after a string
# lstrip() and rstrip() also work for left and right side whitespace

# =============Split Method================
mystring = "Hello, My name is Helal, welcome"
print(mystring.split(','))  # Make list where get comma(,)
mystring = "Hello welcome to python learning"
print(mystring.split(' '))  # Make list where get space (' ')
mystring = "apple#banana#orange#mango"
print(mystring.split('#'))  # Make a list where get hash ('#')
print(mystring.split("#", 2))  # Make a list for first two item
mystring = "Hello welcome \n my name is helal"
print(mystring.splitlines())  # Make a list for every line

# rsplit() and lsplit() both are same as split() only for right and left.


# ====================Join Method==================================

# Join method is complete opposite of split() method

mylist = ["apple", "banana", "orange"]  # List
print("#".join(mylist))
print(" ".join(mylist))
mytuple = ("apple", "banana", "orange")  # Tuple
print(",".join(mytuple))
mydict = {"fruit": "apple", "vegetable": "tomato"}
myseperator = "|"
print(myseperator.join(mydict))
